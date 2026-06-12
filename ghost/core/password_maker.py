import string
import secrets
import json
import random
from datetime import datetime
from colorama import Fore, init
from pathlib import Path

init()
filepath = FILEPATH = Path(__file__).parent.parent / "data" / "pwd.json"

def store_pwd(pwd, username, appname, force=False):
    length = len(pwd)

    if length < 9:
        print(Fore.RED + '[ WEAK ] Password length must be atleast 9.' + Fore.RESET)
        return

    try:
        with open(filepath, "r") as f:
            flag = False
            content = json.load(f)

            if appname in content["myPwd"]:
                for account in content["myPwd"][appname]:
                    if account["username"] == username:
                        if str(force) == "True":
                            account["pwd"] = pwd
                        else:
                            print(Fore.RED + "[ ERROR ] Account already exist!" + Fore.RESET)
                        flag = True   
                if(flag == False):
                    content["myPwd"][appname].append(
                        {
                            "username": username,
                            "pwd": pwd,
                            "createdOn": datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
                        }
                    )
            else:
                content["myPwd"][appname] = [{
                        "username": username,
                        "pwd": pwd,
                        "createdOn": datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
                    }]
        with open(FILEPATH, "w") as f:
            json.dump(content, f, indent=4)
    except Exception as e:
        with open(FILEPATH, "w") as f:
            new_data = {
                "myPwd": {
                    appname: [
                        {
                            "username": username,
                            "pwd": pwd,
                            "createdOn": datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
                        }
                    ]
                }
            }
            json.dump(new_data, f, indent=4)
    print(Fore.GREEN + "[ INF0 ] Password saved!" + Fore.RESET)

def gen_pwd(length=None):
    if length == None:
        length = random.randint(14, 20)
        
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers   = string.digits
    symbols   = string.punctuation

    all_chars = lowercase + uppercase + numbers + symbols

   
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]   

    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))
        secrets.SystemRandom().shuffle(password)
    
    pwd = ''.join(password)
    print(f"Suggested pwd: {pwd}")
    print(f"Length: {length}")
    return pwd

def pwd_strength(pwd: str) -> None:
    score = 0

    if(len(pwd) < 9):
        score += 0
    elif(len(pwd) <= 14 and len(pwd) >= 9):
        score += 1.0
        
    elif(len(pwd) >= 14 and len(pwd) < 16):
        score += 2.0
        
    elif(len(pwd) >= 16):
        score += 4.0
        

    if any(c.islower() for c in pwd):
        score += 1.5
        
    if any(c.isupper() for c in pwd):
        score += 1.5
        
    if any(c.isdigit() for c in pwd):
        score += 1.5
        
    if any(c in string.punctuation for c in pwd):
        score += 1.5
        



    if(score < 5.0):
        print(Fore.RED + "[ WEAK ] Password is weak!" + Fore.RESET)
        print(f"SCORE: {score} / 10")
        print(Fore.BLUE + "TIP: Type 'ghost pwd suggest' to get a strong suggested password!" + Fore.RESET)
    elif(score < 8.0):
        print(Fore.YELLOW + "[ AVERAGE ] Password is average!" + Fore.RESET)
        print(f"SCORE: {score} / 10")
        print(Fore.BLUE + "TIP: Type 'ghost pwd suggest' to get a strong suggested password!" + Fore.RESET)
    else:
        print(Fore.GREEN + "[ STRONG ] Password is strong!" + Fore.RESET)
        print(f"SCORE: {float(score)} / 10")




if __name__ == "__main__":
    #generate_password(int(input("Enter length: ")), input("Enter username: "), input("Enter appname: "), input("Enter flag: "))
    pwd = gen_pwd(8)
    pwd_strength(pwd)
    store_pwd(pwd, "joshiakash514@gmail.com", "instagram", True)

#def strength_checker(pwd):




            











# try:
#     length = int(input('Enter length of password: '))
#     print(f'Generated Password: {generate_password(length)}')

# except ValueError:
#     print('Error, Invalid input.')
    