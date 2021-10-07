from pyfade import Fade, Colors
from pycenter import center
import requests
import json
import os

def main():

    os.system("mode 150, 50")
    os.system("title Kat Graber - Valentin.Lvr")

    
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

    class Col:
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

    McSkinGraber = """
     /$$   /$$             /$$            /$$$$$$                     /$$                          
    | $$  /$$/            | $$           /$$__  $$                   | $$                          
    | $$ /$$/   /$$$$$$  /$$$$$$        | $$  \__/  /$$$$$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
    | $$$$$/   |____  $$|_  $$_/        | $$ /$$$$ /$$__  $$|____  $$| $$__  $$ /$$__  $$ /$$__  $$
    | $$  $$    /$$$$$$$  | $$          | $$|_  $$| $$  \__/ /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
    | $$\  $$  /$$__  $$  | $$ /$$      | $$  \ $$| $$      /$$__  $$| $$  | $$| $$_____/| $$      
    | $$ \  $$|  $$$$$$$  |  $$$$/      |  $$$$$$/| $$     |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      
    |__/  \__/ \_______/   \___/         \______/ |__/      \_______/|_______/  \_______/|__/      
                                                                                              
    """

    def clear():
        os.system("cls")


    def title():
        print(Fade.Vertical(Colors.blue_to_white, center(McSkinGraber)))
        print(Fade.Horizontal(Colors.blue_to_white, center("\nValentin.Lvr")))

    clear()

    sg = skingrabber()

    title()

    print("\n\n\n\n\n\n\n") #Saut de ligne
    username = input(Col.blue+" Username > "+Col.white)
    uuid = sg.get_uuid(user=username)

    os.system("title Kat Graber - Downloading")
    clear()
    title()
    print("\n\n\n\n\n\n\n") #Saut de ligne
    print(Col.blue+f" UUID of "+Col.white+username+" -> "+Col.yellow+uuid)

    skin = sg.get_skin(user=username)

    img_data = requests.get(skin).content
    with open(username + ".png", 'wb') as handler:
        handler.write(img_data)

    os.system("title Kat Graber - Downloaded")
    print("")
    print(Col.green + " Skin downloaded" + Col.white + " - " + Col.blue + "Return in the script folder ;)")
    input()
    main()

if __name__ == "__main__":
    main()
