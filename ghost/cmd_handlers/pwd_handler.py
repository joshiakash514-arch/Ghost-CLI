from ghost.core.password_maker import(
    store_pwd,
    gen_pwd,
    pwd_strength
)

def pwd_handler(args):
    if(args.action == "save"):
        store_pwd(
            args.my_pwd,
            args.username,
            args.appname,
            args.force
        )
    elif(args.action == "suggest"):
        gen_pwd(
            args.l
        )
    elif(args.action == "strength"):
        pwd_strength(
            args.pwd
        )