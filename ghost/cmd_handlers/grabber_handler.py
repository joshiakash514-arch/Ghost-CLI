from ghost.core.grabber import(
    content_grab,
    source_grab
)

def grabber_handler(args):
    if(args.action == "cgrab"):
        content_grab(
            args.url,
            args.tag,
            args.filename,
            args.path
        )
    elif(args.action == "sgrab"):
        source_grab(
            args.url,
            args.filename,
            args.path
        )