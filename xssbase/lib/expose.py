from pyngrok import ngrok, conf
import xssbase.lib.var as var

def router(args):
    args=args.split()
    if(var.var_webserverStarted==True or "force" in args):
        if(len(args)<1):
            print(var.var_exposedServices)
            return 
        if(args[0]=='ngrok'):
            print(len(args))
            if(len(args)>1):
                port=int(args[1])
            else:
                port=var.var_webserverLocalPort
            print("Will run ngrok with port : "+str(port))
            exposed=startNgrok(port)
            var.var_exposedServices=exposed
            print("Started !")
            return
    else:
        print("Need to start webserver first")

def startNgrok(port):
    conf.get_default().ngrok_path = "/usr/bin/ngrok"
    http_tunel=ngrok.connect(addr=port)
    tunnels=ngrok.get_tunnels()

    toReturn=[]
    for t in tunnels:
        toReturn.append(t.public_url)
    return toReturn

