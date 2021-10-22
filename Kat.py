import time
import requests
import json
import os

try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except:
    os.system("pip3 install pystyle")
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

banner = r"""
 ▄▀▀▄ █  ▄▀▀█▄   ▄▀▀▀█▀▀▄ 
█  █ ▄▀ ▐ ▄▀ ▀▄ █    █  ▐ 
▐  █▀▄    █▄▄▄█ ▐   █     
  █   █  ▄▀   █    █      
▄▀   █  █   ▄▀   ▄▀       
█    ▐  ▐   ▐   █         
▐               ▐

  Skin Downloader
"""[1:]

Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, enter=True)

def main(): # FONCTION PRINCIPALE

    clear()
    
    class skingrabber:

        def __init__(self):
            self.url = "https://api.mojang.com/users/profiles/minecraft/"

        def get_uuid(self, user):

            response = requests.get(self.url + user)
            if response.status_code != 200:
                pass
            else:
                responsejson = json.loads(response.content)

                uuid = responsejson["id"]
                return uuid

        def get_skin(self, user):

            response = requests.get(self.url + user)
            if response.status_code != 200:
                pass
            else:
                responsejson = json.loads(response.content)

                uuid = responsejson["id"]
                return f"https://crafatar.com/skins/{uuid}"

    class Col: # COULEURS UwU
        colors = {"red" : "\033[38;2;255;0;0m", 
                "blue" : "\033[38;2;56;152;219m", 
                "yellow" : "\033[38;2;255;255;0m",
                "white" : "\033[38;2;255;255;255m",
                "green" : "\033[38;2;46;204;113m"}

        red = colors['red']

        blue = colors['blue']

        yellow = colors['yellow']
        
        white = colors['white']

        green = colors['green']


    sg = skingrabber()

    print("")
    username = input(f"{Col.blue} ~ Username > {Col.white}")
    uuid = sg.get_uuid(user=username)
    print("")
    print(f"{Col.white} ~ {username}'s {Col.blue}UUID -> {Col.yellow}{uuid}")
    

    skin = sg.get_skin(user=username)

    img_data = requests.get(skin).content
    with open(username + ".png", 'wb') as handler: # ON "ECRIT" LE SKIN SUR UN FICHIER .png
        handler.write(img_data)

    print("")
    print(f"{Col.green} ~ Skin downloaded\n")
    input()
    clear()
    quit()

if __name__ == "__main__":
    main() # EXECUTION DE LA FONCTION "MAIN"
