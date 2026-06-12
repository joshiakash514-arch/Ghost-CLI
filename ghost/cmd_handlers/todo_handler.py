from ghost.core.todo import (
    add_task,
    view_todo,
    task_start,
    delete_task,
    reset_todo,
)

def todo_handler(args):
    if(args.action == "add"):
        add_task(
            args.name,
            args.target_minutes
        )
    elif(args.action == "list"):
        view_todo()
    elif(args.action == "start"):
        task_start(
            args.task_id
            )
    elif(args.action == "rm"):
        delete_task(
            args.task_id,
            args.force
        )
    elif(args.action == "reset"):
        reset_todo(
            args.force
        )
