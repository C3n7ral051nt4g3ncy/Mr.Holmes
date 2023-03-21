#!/usr/bin/python3
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
from Core.Support import Menu
from Core.Support import Font
from Core.Support import Language

filename = Language.Translation.Get_Language()
filename

class Main:

    @staticmethod
    def Controll_Display():
        Interface_file = "Display/Display.txt"
        if os.path.isfile(Interface_file):
            with open(Interface_file,"r",newline=None) as d:
                conf = d.read().strip("\n")
            if conf not in ["Desktop", "Mobile"]:
                print(
                    f"{Font.Color.RED}[!]{Font.Color.WHITE}"
                    + Language.Translation.Translate_Language(
                        filename, "Default", "DisplayError", "None"
                    )
                )
                exit()
        else:
            print(
                f"{Font.Color.RED}[!]{Font.Color.WHITE}"
                + Language.Translation.Translate_Language(
                    filename, "Default", "NoDisplay", "None"
                ).format(Interface_file)
            )
        return conf

    def Menu(self):
        Menu.Main.main(self)

if __name__ == "__main__":
    Mode = Main.Controll_Display()
    Mode
    try:
       Main.Menu(Mode)
    except KeyboardInterrupt:
        print(Font.Color.RED + "\n\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "KeyC", "None"))
        exit()
    except ModuleNotFoundError as Error:
        print(Font.Color.RED + "\n\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Internal", "None").format(str(Error)))
        exit()
