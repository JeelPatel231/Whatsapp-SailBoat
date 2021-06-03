import main

# i know this is straight on eval function, so you can execute a 
# bunch of things from here, even control the bot using whatspp itself
# by executing functions from main.py

def calc(args):
    if args == "":
        main.send_msg("```evaluated the Void!```")
    else:
        main.send_msg(str(eval(args)))

def help():
    main.send_msg("```calculates stuff for your lazy ass```")