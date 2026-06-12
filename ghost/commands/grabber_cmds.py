def grabber_parse(subparser):
    grabber_parser = subparser.add_parser("grabber")
    grabber_subparser = grabber_parser.add_subparsers(
        dest="action",
        required=True
    )

    content_grab = grabber_subparser.add_parser(
        "cgrab",
        help="Grab the content of any webpage."
    )

    content_grab.add_argument(
        "url",
        help="URL of target website."
    )

    content_grab.add_argument(
        "tag",
        help="HTML tag of taget website"
    )

    content_grab.add_argument(
        "--filename",
        help="Filename to save grabbed data."
    )

    content_grab.add_argument(
        "--path",
        help="Filepath to store created file."
    )

    source_grab = grabber_subparser.add_parser(
        "sgrab",
        help="Grab the source code of the webpage."
    )
    source_grab.add_argument(
        "url",
        help="URL of target website."
    )

    source_grab.add_argument(
        "--filename",
        help="Filename to save grabbed data."
    )

    source_grab.add_argument(
        "--path",
        help="Filepath to store created file."
    )

    return grabber_parser