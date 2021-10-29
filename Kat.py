import requests
import json
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    
def center(var: str, space: int = None, icon: str = " ", sep: bool = False):
    if not space:
        space = (os.get_terminal_size().columns -
                len(var.splitlines()[int(len(var.splitlines())/2)])) / 2

    if not sep:
        return "\n".join((icon * int(space)) + var for var in var.splitlines())
    else:
        return "\n".join((icon * int(space)) + var + (icon * int(space)) for var in var.splitlines())

banner = """
 ▄▀▀▄ █  ▄▀▀█▄   ▄▀▀▀█▀▀▄
█  █ ▄▀ ▐ ▄▀ ▀▄ █    █  ▐
▐  █▀▄    █▄▄▄█ ▐   █
  █   █  ▄▀   █    █
▄▀   █  █   ▄▀   ▄▀
█    ▐  ▐   ▐   █
▐               ▐
"""

def main():

    clear()

    

    class skingrabber:

        def __init__(self):
            self.url = "https://api.mojang.com/users/profiles/minecraft/"


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
                "white" : "\033[38;2;255;218;185m",
                "green" : "\033[38;2;46;204;113m"}

        red = colors['red']

        blue = colors['blue']

        yellow = colors['yellow']

        white = colors['white']

        green = colors['green']

    sg = skingrabber()


    print(Col.blue + center(banner))
    print(Col.blue + center("\nValentin.Lvr"))
    print("\n\n\n")
    username = input(f"{Col.blue} ~ Username > {Col.white}")

    skin = sg.get_skin(user=username)

    try:
        img_data = requests.get(skin).content

    except:
        print()
        print(f"{Col.red} ~ This user do not exist")
        input()
        main()

    with open(username + ".png", 'wb') as handler:
        handler.write(img_data)


    print("")
    print(f"{Col.green} ~ Skin downloaded\n")
    print(f"{Col.green} ~ GitHub : {Col.white}github.com/ValentinLvrr")
    print(f"{Col.green} ~ Discord : {Col.white}ValentinLvr#7112\n")
    input()
    clear()
    quit()

if __name__ == "__main__":
    main()
