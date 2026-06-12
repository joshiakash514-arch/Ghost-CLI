def pwd_parser(subparser):
    pwd_parser = subparser.add_parser("pwd")
    pwd_subparser = pwd_parser.add_subparsers(
        dest="action",
        required=True
    )

    store_pwd = pwd_subparser.add_parser(
        "save",
        help="Save passwords in a file."
    )

    store_pwd.add_argument(
        "my_pwd",
        help="Password to be saved."
    )

    store_pwd.add_argument(
        "username",
        help="Username of the user."
    )

    store_pwd.add_argument(
        "appname",
        help="Site name where the stored password is to be used."
    )

    store_pwd.add_argument(
        "--force",
        help="Bypass all warns and store the password.",
        action="store_true"
    )

    gen_pwd = pwd_subparser.add_parser(
        "suggest",
        help="Generate a random strong password."
    )
    gen_pwd.add_argument(
        "-l",
        help="length of the password.",
        type=int
    )

    pwd_strength = pwd_subparser.add_parser(
        "strength",
        help="Check the strength of the password."
    )

    pwd_strength.add_argument(
        "pwd",
        help="Password to be checked."
    )

    return pwd_parser
