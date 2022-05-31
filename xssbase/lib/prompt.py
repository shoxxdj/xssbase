from cmd import Cmd
from xssbase.lib.expose import router as expose_router
from xssbase.lib.webserver import router as webserver_router
from xssbase.lib.payload import router as payload_router
import xssbase.lib.var as var

class MyPrompt(Cmd):

    prompt = '[XSSBASE] '

    def do_exit(self, inp):
        print("Bye")
        return True

    def emptyline(self):
        return 

    def do_webserver(self,args):
        'webserver local_port ex: webserver 8080'
        webserver_router(args)

    def do_expose(self,args):
        'expose [ngrok local_port][otherservice otherarg] ex: expose ngrok 8080'
        expose_router(args)

    def do_payload(self,args):
        payload_router(args)

    def do_vars(sefl,args):
        print(var.var_exposedServices)
        print(var.var_webserverStarted)
        print(var.var_webserverLocalPort)

   
def start():
    MyPrompt().cmdloop()

