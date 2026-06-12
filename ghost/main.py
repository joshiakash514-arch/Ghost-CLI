import argparse
from ghost.commands import (
    todo_cmds,
    grabber_cmds,
    pwd_cmds,
    sorter_cmds
)
from ghost.cmd_handlers import (
    todo_handler,
    grabber_handler,
    pwd_handler,
    sorter_handler
)

def main():
    parser = argparse.ArgumentParser(
        prog="ghost",
        description="Ghost is a multipurpose CLI tool containing various features by which you can handle your daily tasks."
    )
    # Subparser containes all major modules like -> todo, grabber etc
    subparser = parser.add_subparsers(
        dest="module",
        required=True
    )

    # Register modules
    todo_parser = todo_cmds.todo_parse(subparser)
    grabber_parser = grabber_cmds.grabber_parse(subparser)
    pwd_parser = pwd_cmds.pwd_parser(subparser)
    sorter_parser = sorter_cmds.sorter_parser(subparser)

    # Attach handlers
    todo_parser.set_defaults(
        func=todo_handler.todo_handler
    )

    grabber_parser.set_defaults(
        func=grabber_handler.grabber_handler
    )

    pwd_parser.set_defaults(
        func=pwd_handler.pwd_handler
    )

    sorter_parser.set_defaults(
        func=sorter_handler.sorter_handler
    )

    # Code chlane k lie
    args = parser.parse_args()
    args.func(args)





if __name__ == "__main__":
    main()
