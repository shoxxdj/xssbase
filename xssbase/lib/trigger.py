import xssbase.lib.var as var
import xssbase.lib.logger as log

def router(args):
	args=args.split()

	triggerFind=False

	for arg in args: 
		if(arg.upper() in TRIGGER):
			triggerFind=True
			var.var_trigger=TRIGGER[arg.upper()]
			return 

	if not triggerFind:
		print(', '.join([k.lower() for k in TRIGGER.keys()]))


TRIGGER={}
TRIGGER['SCRIPT']="<script>%s</script>"
TRIGGER['AUDIO']='<audio src onloadstart="%s">'
