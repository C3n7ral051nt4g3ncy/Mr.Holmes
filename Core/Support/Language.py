# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import json
import os
from configparser import ConfigParser


class Translation:

    @staticmethod
    def Get_Language():
        Config_file = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(Config_file)
        Lang = Parser["Settings"]["language"]
        filename = f"Lang/{Lang}.json"
        return filename if os.path.isfile(filename) else "Lang/english.json"

    @staticmethod
    def Translate_Language(filename, List, Row, SubRow):
        reader = open(filename, )
        parser = json.loads(reader.read())
        return (
            parser[List][0][Row][SubRow]
            if List in ["Configuration", "Username", "Website", "Report"]
            else parser[List][Row]
        )
