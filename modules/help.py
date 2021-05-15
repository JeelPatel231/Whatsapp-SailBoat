import main

def help(args):
    if args == "":
        modlist='Available Modules : \n\n'
        for i in main.mods:
            if i == "help":
                pass
            else:
                modlist=modlist+ "• " +i+"\n"
        main.send_msg(modlist)
    else:
        main.helpinside(args)