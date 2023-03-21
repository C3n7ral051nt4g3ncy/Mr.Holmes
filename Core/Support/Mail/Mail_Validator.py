# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import re as Regex
from Core.Support import Font
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename

class Validator:

      @staticmethod
      def Mail(username, report):
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                 Language.Translation.Translate_Language(filename, "Email", "Check", "None").format(username))
            sleep(3)
            simbols = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if Regex.fullmatch(simbols, username):
                  print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}" +
                        Language.Translation.Translate_Language(filename, "Email",
                                                                "Valid", "None"))
                  f = open(report, "a")
                  f.write("\n\nTHIS EMAIL IS VALID")
                  f.close
                  with open("Temp/E-Mail/Code.txt", "w") as f:
                        f.write("Is-Valid")
            else:
                  print(f"{Font.Color.RED}[!]{Font.Color.WHITE}" +
                        Language.Translation.Translate_Language(filename, "Email",
                                                                "NotValid", "None"))
                  with open(report, "a") as f:
                        f.write("\n\nTHIS EMAIL IS NOT VALID")
                  inp = input(Language.Translation.Translate_Language(filename, "Default", "Continue", "None"))
