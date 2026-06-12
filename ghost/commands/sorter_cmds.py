def sorter_parser(subparser):
    sorter_parser = subparser.add_parser(
        "sort",
        help="Can be used to sort files and folders."
    )

    sorter_parser.add_argument(
        "path",
        help="Path to be sorted."
    )

    return sorter_parser