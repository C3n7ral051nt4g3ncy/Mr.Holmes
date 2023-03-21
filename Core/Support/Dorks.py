# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Support import Font
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename


class Search:

    @staticmethod
    def dork(username, report, nomefile, Type):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Dorks", "Generation", "None").format(Type))
        sleep(2)
        username = username.replace(" ","+")
        with open(report, "a") as f:
            f.write(Type + "-DORKS:\n\n")
        with open(nomefile, "r") as f:
            for sites in f:
                site = sites.rstrip("\n")
                site = site.replace("{}", username)
                print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}{site}")
                sleep(2)
                f = open(report, "a")
                f.write(site + "\n")
        f.close()
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename,
              "Default", "Report", "None") + report)

    @staticmethod
    def Generator(Type,nomefile,report,phrase):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Dorks", "Generation", "None").format(Type))
        sleep(2)
        """if Type == "YANDEX":
            phrase = phrase.replace(" ", "%2B")
        else:"""
        phrase = phrase.replace(" ","+")
        with open(report, "a") as f:
            f.write("\n" + Type + "-DORKS:\n\n")
        with open(nomefile, "r") as f:
            for sites in f:
                site = sites.rstrip("\n")
                site = site.replace("{}", phrase)
                print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}{site}")
                sleep(2)
                f = open(report, "a")
                f.write(site + "\n")
        f.close()
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename,
              "Default", "Report", "None") + report)

