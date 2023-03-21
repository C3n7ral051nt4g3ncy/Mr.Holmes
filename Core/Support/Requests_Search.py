# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import requests
import json
from Core.Support import Font
from Core.Support import Language

filename = Language.Translation.Get_Language()
filename


class Search:

    @staticmethod
    def search(error, report, site1, site2, http_proxy, sites, data1, username, subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2, Tag, Tags):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        searcher = requests.get(
            url=site2, headers=headers, proxies=http_proxy, timeout=10, allow_redirects=True)
        f = open(report, "a")
        if error == "Status-Code":
            if searcher.status_code == 200:
                print(
                    (
                        f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Default", "Found", "None"
                        ).format(subject, username)
                    )
                )
                print(
                    (
                        Font.Color.YELLOW
                        + "[v]"
                        + Font.Color.WHITE
                        + f"LINK: {site1}"
                    )
                )

                if Writable == True:
                    f.write(site1 + "\r\n")
                    print(
                        (
                            Font.Color.BLUE
                            + "[I]"
                            + Font.Color.WHITE
                            + f"TAGS:[{Font.Color.GREEN + Tag + Font.Color.WHITE}]"
                        )
                    )
                    Tags.append(Tag)
                else:
                    f.write(f"{name}:{main}\r\n")
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)
            elif searcher.status_code in [404, 204]:
                print(
                    (
                        f"{Font.Color.RED}[!]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Default", "NotFound", "None"
                        ).format(subject, username)
                    )
                )
            else:
                print(
                    (
                        f"{Font.Color.BLUE}[N]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Default", "Connection_Error2", "None"
                        )
                    )
                )
        elif error == "Message":
            text = sites[data1]["text"]
            if text in searcher.text:
                print(
                    (
                        f"{Font.Color.RED}[!]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Default", "NotFound", "None"
                        ).format(subject, username)
                    )
                )
            else:
                print(
                    (
                        f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Default", "Found", "None"
                        ).format(subject, username)
                    )
                )
                print(
                    (
                        Font.Color.YELLOW
                        + "[v]"
                        + Font.Color.WHITE
                        + f"LINK: {site1}"
                    )
                )
                if Writable == True:
                    f.write(site1 + "\r\n")
                    print(
                        (
                            Font.Color.BLUE
                            + "[I]"
                            + Font.Color.WHITE
                            + f"TAGS:[{Font.Color.GREEN + Tag + Font.Color.WHITE}]"
                        )
                    )
                    Tags.append(Tag)
                else:
                    f.write(f"{name}:{main}\r\n")
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)

        elif error == "Response-Url":
            response = sites[data1]["response"]
            if searcher.url == response:
                print(
                    (
                        f"{Font.Color.RED}[!]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Default", "NotFound", "None"
                        ).format(subject, username)
                    )
                )
            else:
                print(
                    (
                        f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Default", "Found", "None"
                        ).format(subject, username)
                    )
                )
                print(
                    (
                        Font.Color.YELLOW
                        + "[v]"
                        + Font.Color.WHITE
                        + f"LINK: {site1}"
                    )
                )
                if Writable == True:
                    f.write(site1 + "\r\n")
                    print(
                        (
                            Font.Color.BLUE
                            + "[I]"
                            + Font.Color.WHITE
                            + f"TAGS:[{Font.Color.GREEN + Tag + Font.Color.WHITE}]"
                        )
                    )
                    Tags.append(Tag)
                else:
                    f.write(f"{name}:{main}\r\n")
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)

        with open(json_file2, "w") as d:
            d.write('''{
                    "Names":[

                    ]
                }''')
        with open(json_file, "w") as f:
            f.write('''{
                    "List":[

                    ]
                }''')
        for element in successfullName:
            data = {"name": f"{element}"}
            with open(json_file2, 'r+') as file2:
                file_data2 = json.load(file2)
                file_data2["Names"].append(data)
                file2.seek(0)
                json.dump(file_data2, file2, indent=4)

        for element in successfull:
            data = {"site": f"{element}"}
            with open(json_file, 'r+') as file:
                file_data = json.load(file)
                file_data["List"].append(data)
                file.seek(0)
                json.dump(file_data, file, indent=4)