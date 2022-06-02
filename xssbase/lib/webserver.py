import cherrypy
import xssbase.lib.var as var


def router(args):
    args=args.split()
    listenPort=0
    if(len(args)>1):
        if(args[0]=='start'):
            listenPort=int(args[1])
        else:
            #Try to find a valid port from list
            #check if available first
            listenPort=8080

        start(listenPort)
        var.var_webserverLocalPort=listenPort
        var.var_webserverStarted=True
        print("GET IP")
        var.var_localServices.append("http://127.0.0.1"+":"+str(listenPort)+"/") 


class GetPostMethods(object):
    @cherrypy.expose
    def default(self,*args,**kwargs):
        print(cherrypy.request.headers)
        if(cherrypy.request.method=="POST"):
            print(cherrypy.request.headers)
            print(kwargs)
        else:
            print("its a get")
        return "It works!"

# def start(port):
#     print("Asked to start")
#     # # Unsubscribe default server
#     # cherrypy.server.unsubscribe()
#     # conf = { '/': {'server.socket_port':1234} }

#     # cherrypy.quickstart(GetPostMethods(), '/', conf)
#     conf = { '/': {} }
#     cherrypy.config.update({
#                 'server.socket_host': '127.0.0.1',
#                 'server.socket_port': port,
#         })
#     t = Thread(target=cherrypy.quickstart(GetPostMethods(), "/", config=conf) , daemon=True)
#     #cherrypy.quickstart(GetPostMethods(), "/", config=conf)
#     t.start() 
#     print("done")
#     return 

def start(port):
    #testconf = path.join(path.dirname(__file__), 'webservertest.conf')
    conf = { '/': {} }
    web_server = GetPostMethods()
    cherrypy.tree.mount(web_server, "", config=conf)
    cherrypy.config.update({
                 'server.socket_host': '127.0.0.1',
                 'server.socket_port': port,
    })
    cherrypy.engine.start()
    return 