import json
import time
import os
import sys
import shutil
from colorama import Fore, init
from pyfiglet import Figlet
from pathlib import Path
from datetime import datetime, timedelta

init()
BORDERS = '='*20 + '[ TODO ]' + '='*20
FILEPATH = Path(__file__).parent.parent / "data" / "tasks.json"
figlet_font1 = Figlet(font="starwars")

# Task adder function
def add_task(name, target_time):
    try:
        with open(FILEPATH ,"r") as f:
            current_data = json.load(f)
            last_id = current_data["tasks"][-1]["id"]
            new_task = {
                "id": last_id + 1,
                "name": name,
                "created": str(datetime.now().strftime("%d-%m-%Y %I:%M %p")),
                "deadline": str((datetime.now() + timedelta()).strftime("%d-%m-%Y 10:00 PM")),
                "target_minutes": target_time,
                "completed_minutes": 0,

                "IsCompleted": False
            }
            current_data["tasks"].append(new_task)
        with open(FILEPATH, 'w') as f:
            json.dump(current_data, f, indent=4)
    except:
        new_task = {
            "tasks": [ 
                 {
                    "id": 1,
                    "name": name,
                    "created": str(datetime.now().strftime("%d-%m-%Y %I:%M %p")),
                    "deadline": str((datetime.now() + timedelta()).strftime("%d-%m-%Y 10:00 PM")),
                    "target_minutes": target_time,
                    "completed_minutes": 0,
                    "IsCompleted": False
                }
            ]
        }
        
        with open(FILEPATH, 'w') as f:
             json.dump(new_task, f, indent=4)
    print(Fore.GREEN + "[ INFO ] Task created successfully!" + Fore.RESET)

# View Tasks
def view_todo():
    try:
        with open(FILEPATH, "r") as f:
            content = json.load(f)["tasks"]
            if content:
                print(f"{"TASK ID":<19}{"STATUS":<19}{"TASK NAME":<19}{"DEADLINE":<30}{"REMAINING TARGET TIME":<19}")
                for data in content:
                    if(data["IsCompleted"] == True):
                        print(
                            f"{data["id"]:<19}"
                            f"{"[ DONE ]":<19}"
                            f"{data["name"]:<19}"
                            f"{"NONE":<30}"
                            f"NONE"
                        )
                    else:
                        print(
                            f"{data["id"]:<19}"
                            f"{"[ NOT DONE ]":<19}"
                            f"{data["name"]:<19}"
                            f"{data["deadline"]:<30}"
                            f"{data["target_minutes"]-data["completed_minutes"]:<19}"
                        )
            else:
                print(Fore.RED + "[ ERROR ] Task list is empty..." + Fore.RESET)
    except:
        print(Fore.RED + "[ ERROR ] File not found!" + Fore.RESET)  

# Start task
def task_start(task_id):
    with open(FILEPATH, "r") as f:
        content = json.load(f)
    
    task_found = False
    for task in content["tasks"]:
        if task["id"] == task_id:
            task_found= True
            previous_progress = task["completed_minutes"]
            start_time = time.time()
            print(Fore.GREEN + f"[+] Started {task["name"]}!" + Fore.RESET)
            try:
                target_seconds = task["target_minutes"] * 60
                while True:
                    elapsed_secconds = int(time.time() - start_time)
                    completed_seconds = (
                        previous_progress * 60 + elapsed_secconds
                    )

                    # Task complete
                    if(completed_seconds >= target_seconds):
                        task["completed_minutes"] = task["target_minutes"]
                        task["IsCompleted"] = True

                        with open(FILEPATH, "w") as f:
                            json.dump(content, f, indent=4)

                        show_dashboard(
                            task["name"],
                            completed_seconds,
                            task["target_minutes"] * 60
                        )

                        print(Fore.GREEN + "\n[+] Task Completed!" + Fore.RESET)
                        return
                    
                    # Update Progress
                    task["completed_seconds"] = completed_seconds
                    task["completed_minutes"] = completed_seconds // 60

                    with open(FILEPATH, "w") as f:
                        json.dump(content, f, indent=4)
                    
                    show_dashboard(
                        task["name"],
                        completed_seconds,
                        task["target_minutes"] * 60
                    )
                    time.sleep(1)

            except KeyboardInterrupt:
                with open(FILEPATH, "w") as f:
                    json.dump(content, f, indent=4)
                
                print(Fore.RED + "\n\n[ ERROR ] Task stopped manually." + Fore.RESET)
                return
            
    if not task_found:
        print(Fore.RED + "[ ERROR ] Task not found!" + Fore.RESET)

# Delete a specific task
def delete_task(id_to_delete, confirmation):
    flag = False

    with open(FILEPATH, "r") as f:
        content = json.load(f)

        if content["tasks"]:
            for task_id in range(0, len(content["tasks"])):
                if(content["tasks"][task_id]["id"] == id_to_delete):
                    if confirmation:
                        removed = content["tasks"].pop(task_id)
                        print(f"{"TASK ID":<19}{"STATUS":<19}{"TASK NAME":<19}{"DEADLINE":<30}{"REMAINING TARGET TIME":<19}")
                        
                        if(removed["IsCompleted"] == True):
                            print(Fore.RED +
                                f"{removed["id"]:<19}"
                                f"{"[ DONE ]":<19}"
                                f"{removed["name"]:<19}"
                                f"{"NONE":<30}"
                                f"NONE" +
                                Fore.RESET
                            )
                        else:
                            print(Fore.RED +
                                f"{removed["id"]:<19}"
                                f"{"[ NOT DONE ]":<19}"
                                f"{removed["name"]:<19}"
                                f"{removed["deadline"]:<30}"
                                f"{removed["target_minutes"]-removed["completed_minutes"]:<19}" +
                                Fore.RESET
                            )

                        with open(FILEPATH, "w") as f:
                            json.dump(content, f, indent=4)

                        print(Fore.GREEN + "[ INFO ] Task removed successfully!" + Fore.RESET)
                    else:
                        print(Fore.RED + "[ ERROR ] Provide confirmation!" + Fore.RESET)
                    return
        else:
            print(Fore.RED + "[ ERROR ] Task list is empty..." + Fore.RESET) 
            return

    print(Fore.RED + "[ ERROR ] Task not found!" + Fore.RESET)
    return

# Reser Todo by deleting .json file
def reset_todo(confirmation):
    if os.path.exists(FILEPATH):
        if confirmation:
            os.remove(FILEPATH)
            print(Fore.GREEN + "[ INFO ] Tasks resetted successfully" + Fore.RESET)
        else:
            print(Fore.RED + "[ ERROR ] Provide confirmation!" + Fore.RESET)
    else:
        print(Fore.RED + "[ ERROR ] Tasks.json does not exist!" + Fore.RESET)
    return

# Dashboard with timer
def show_dashboard(task_name, completed_seconds, target_seconds):
    remaining_seconds = max(
        target_seconds - completed_seconds, 0
    )
    hours = remaining_seconds // 3600
    minutes = (remaining_seconds % 3600)//60
    seconds = remaining_seconds % 60

    progress = min(completed_seconds / target_seconds, 1)
    filled = int(progress * 20)
    bar = "█" * filled + '░' * (20 - filled)
    os.system("cls" if os.name == "nt" else "clear")


    timer = f"{hours:02} : {minutes:02} : {seconds:02}"
    timer_art = figlet_font1.renderText(timer)
    
    lines = []
    lines.append("===============================================\n")
    lines. append(f"Task: {task_name}\n")
    lines.append("===============================================\n")
    lines.append("")

    for line in timer_art.splitlines():
        lines.append(line)
    
    lines.append("")
    lines.append(f"[{bar}] {progress * 100:.2f}%\n")
    lines.append(
        f"Progress: "
        f"{completed_seconds // 60}"
        f" / {target_seconds // 60} min"
    )
    center(lines)

# Align dashboard to center
def center(text):
    terminal = shutil.get_terminal_size()
    width = terminal.columns
    height = terminal.lines
    top_padding = max(0, (height - len(text)) // 2)
    print("\n" * top_padding)

    for line in text:
        print(line.center(width))







