# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import random
from Core.Support import Font
from Core.Support import Language

filename = Language.Translation.Get_Language()
filename


class Random:

    def Get_Banner(self, Mode):
        if Mode == "Desktop":
            List = ["Banner1.txt", "Banner2.txt", "Banner3.txt"]
        elif Mode == "Mobile":
            List = ["Banner4.txt", "Banner5.txt"]
        else:
            print(
                (
                    f"{Font.Color.RED}[!]{Font.Color.WHITE}"
                    + Language.Translation.Translate_Language(
                        filename, "Default", "DisplayError", "None"
                    )
                )
            )
            exit()
        choice = random.choice(List)
        with open(f"{self}/{choice}", "r", newline=None) as f:
            banner = f.read()
        print(Font.Color.GREEN + banner)
