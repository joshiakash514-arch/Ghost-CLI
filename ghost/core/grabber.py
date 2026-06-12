import colorama
import requests
import os
from pathlib import Path
from bs4 import BeautifulSoup


colorama.init()
# Taking user defined website

def content_grab(URL, tag_to_find, filename, path):
    header = {
        "User-Agent": "Mozilla/5.0" 
    }

    # Sending request
    try:
        response = requests.get(URL, headers=header, timeout=10)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print(colorama.Fore.RED + "[ ERROR ] No internet connection!" + colorama.Fore.RESET)
        return
    except requests.exceptions.Timeout:
        print(colorama.Fore.RED + "[ ERROR ] Request timed out!" + colorama.Fore.RESET)
        return
    except requests.exceptions.HTTPError as e:
        print(colorama.Fore.RED + f"[ ERROR ] HTTP Error: {e}!" + colorama.Fore.RESET)
        return
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED + f"[ ERROR ] Request failed: {e}!" + colorama.Fore.RESET)
        return


    # Converting html to text
    soup = BeautifulSoup(response.text, "html.parser")

    # Storing the the text to database 
    newPath = os.path.join(Path.home(), path, filename)

    if filename:
        if newPath:
            if not os.path.exists(newPath):
                with open(newPath, 'w', encoding='utf-8') as f:
                    for data in soup.find_all(tag_to_find):
                        f.write(data.text)
                    print(colorama.Fore.GREEN + "[ INFO ] Done!!!" + colorama.Fore.RESET)
            else:
                print(colorama.Fore.RED + '[ERROR] File with that name alreay exist!' + colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED + "[ ERROR ] Specify filepath!" + colorama.Fore.RESET)
    else:
        for data in soup.find_all(tag_to_find):
            print(data.text)
    print(colorama.Fore.GREEN + "\n[ INFO ] Done!!!" + colorama.Fore.RESET)
    return


def source_grab(URL, PATH, filename):
    # Taking user defined website
    header = {
        "User-Agent": "Mozilla/5.0" 
    }

    # Sending request
    try:
        response = requests.get(URL, headers=header, timeout=10)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print(colorama.Fore.RED + "[ ERROR ] No internet connection!" + colorama.Fore.RESET)
        return
    except requests.exceptions.Timeout:
        print(colorama.Fore.RED + "[ ERROR ] Request timed out!" + colorama.Fore.RESET)
        return
    except requests.exceptions.HTTPError as e:
        print(colorama.Fore.RED + f"[ ERROR ] HTTP Error: {e}!" + colorama.Fore.RESET)
        return
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED + f"[ ERROR ] Request failed: {e}!" + colorama.Fore.RESET)
        return

    # Storing the the text to database 
    newPath = os.path.join(Path.home(), PATH.join(".html"), filename)

    if filename:
        if newPath:
            try:
                with open(newPath, 'w', PATH,  encoding='utf-8') as f:
                    f.write(response.text)
                    print(colorama.Fore.GREEN + "[ INFO ] Done!!!" + colorama.Fore.RESET)
            except:
                print(colorama.Fore.RED + 'File with that name alreay exist!' + colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED + "[ ERROR ] Specify filepath!" + colorama.Fore.RESET)
    else:
        print(response.text)
        print(colorama.Fore.GREEN + "\n[ INFO ] Done!!!" + colorama.Fore.RESET)
    
    return
        
