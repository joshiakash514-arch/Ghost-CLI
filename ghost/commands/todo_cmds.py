def todo_parse(subparser):
    # todo_parser containes all cmds of todo
    todo_parser = subparser.add_parser("todo")

    # todo_subparser containes inner commands of todo like -> ghost todo add
    todo_subparser = todo_parser.add_subparsers(
        dest="action",
        required=True
    )

    # todo_add containes inner arguments of add like -> ghost todo add "task_name" "time_in_minutes"
    todo_add = todo_subparser.add_parser(
        "add",
        help="Add any task to your todo.",

    )

    # Containes arguments of add cmd
    todo_add.add_argument(
        "name",
        help="Enter name of the task.",
    )
    todo_add.add_argument(
        "target_minutes",
        help="Enter target minutes upto which you will stay on task.",
        type=int,
    )

    # todo_list containes inner arguments of view like 
    todo_list = todo_subparser.add_parser(
        "list",
        help="View all user tasks."
    )

    todo_start = todo_subparser.add_parser(
        "start",
        help="Start any specific task with its id."
    )

    todo_start.add_argument(
        "task_id",
        help="ID of the task to be started.",
        type=int
    )

    # todo_delete containes necessary arguments to delete any task
    todo_delete = todo_subparser.add_parser(
        "rm",
        help="Remove any specific task from the task list."
    )

    todo_delete.add_argument(
        "task_id",
        help="ID of the task to be removed.",
        type=int
    )

    todo_delete.add_argument(
        "--force",
        help="Confirmation to delete any task ( Optional )",
        action="store_true"
    )

    todo_reset = todo_subparser.add_parser(
        "reset",
        help="Completely reset todo list."
    )

    todo_reset.add_argument(
        "--force",
        help="Confirmation to completely reset current todo list.",
        action="store_true"
    )

    return todo_parser
