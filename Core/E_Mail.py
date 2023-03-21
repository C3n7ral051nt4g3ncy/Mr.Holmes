# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import json
import urllib
import MrHolmes as holmes
from Core.Support import Font
from Core.Support import Creds
from Core.Support import FileTransfer
from Core.Support import Clear
from Core.Support import Dorks
from Core.Support.Mail import Mail_Validator as mail
from Core.Support import ApiCheck as Api
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from Core.Support import DateFormat
from Core.Support import Notification
from Core.Support import Encoding
from time import sleep
from datetime import datetime

filename = Language.Translation.Get_Language()
filename


class Mail_search:

    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/E-Mail"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def Google_dork(username):
        report = f"GUI/Reports/E-Mail/Dorks/{username}_dorks.txt"
        nomefile = "Site_lists/E-Mail/Google_dorks.txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Dorks", "Remove", "None").format(username))
        Type = "GOOGLE"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def Yandex_dork(username):
        report = f"GUI/Reports/E-Mail/Dorks/{username}_dorks.txt"
        nomefile = "Site_lists/E-Mail/Yandex_dorks.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def Lookup(username, report):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Website", "Default", "Whois").format(username))
        sleep(2)
        Key = Api.Check.WhoIs()
        Key
        if Key == "None":
            print(f"{Font.Color.RED}[!]{Font.Color.WHITE}API-KEY NOT FOUND")
        else:
            RecList = []
            try:
                print(
                    (
                        f"{Font.Color.GREEN}[+]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Website", "Parameters", "KeyFound"
                        )
                    )
                )
                Key2 = str(Key)
                source = f"https://emailverification.whoisxmlapi.com/api/v2?apiKey={Key2}&emailAddress={username}"
                access = urllib.request.urlopen(source)
                reader = access.read()
                final = json.loads(reader)
                name = final["username"]
                domain = final["domain"]
                completemail = final["emailAddress"]
                dns = final["dnsCheck"]
                freeDomain = final["freeCheck"]
                Temporary = final["disposableCheck"]
                if("smtpCheck" in final):
                    smtp = final["smtpCheck"]
                    SmtpOk = True
                else:
                    SmtpOk = False
                if("catchAllCheck" in final):
                    CatchAll = final["catchAllCheck"]
                    CatchOk = True
                else:
                    CatchOk = False
                if("mxRecords" in final):
                    Records = final["mxRecords"]
                    i = 0
                    for record in Records:
                        RecList.append(record)
                        i = i+1
                    RecordOk = True
                else:
                    RecordOk = False
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "INFORMATIONS FOUND:")
                sleep(3)
                print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}NAME: {name}")
                print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}DOMAIN: {domain}")
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "EMAIL: " + completemail)
                if SmtpOk:
                    print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}SMTP: {smtp}")
                print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}DNS: {dns}")
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "FREE-DOMAIN: " + freeDomain)
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "TEMPORARY: " + Temporary)
                if CatchOk:
                    print(Font.Color.YELLOW +
                        "[v]" + Font.Color.WHITE + "CATCH-ALL: " + CatchAll)
                if RecordOk:
                    print(Font.Color.GREEN +
                        "\n[+]" + Font.Color.WHITE + "FOUND MX-RECORDS(DNS):")
                    i = 1
                    for record in RecList:
                        print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}" + f"RECORD N {i}: " + record)
                        i = i+1
                sleep(2)
                f = open(report, "a")
                f.write("\n\nEMAIL DATA:" + "\r\n")
                f.write(f"NAME: {name}" + "\r\n")
                f.write(f"DOMAIN: {domain}" + "\r\n")
                f.write(f"EMAIL: {completemail}" + "\r\n")
                f.write(f"SMTP: {smtp}" + "\r\n")
                f.write(f"FREE-DOMAIN: {freeDomain}" + "\r\n")
                f.write(f"TEMPORARY: {Temporary}" + "\r\n")
                f.write(f"CATCH-ALL: {CatchAll}" + "\r\n")
                f.write("\n\nFOUND MX-RECORDS(DNS)" + "\r\n")
                i = 1
                for record in RecList:
                    f.write(f"RECORD N {i}: {record}" + "\r\n")
                    i = i+1
            except Exception as e:
                pass

    @staticmethod
    def searcher(username, report, Mode):
        nomefile = "Temp/E-Mail/Code.txt"
        if os.path.isfile(nomefile):
            list_file = "Site_lists/E-Mail/Lists.json"
            reader = open(list_file,)
            data = json.loads(reader.read())
            for sites in data:
                for data1 in sites:
                    name = sites[data1]["name"]
                    url = sites[data1]["url"].replace("{}", username)
                    print(
                        Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Link", "None").format(name))
                    sleep(2)
                    print(f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}{url}")
                    f = open(report, "a")
                    f.write(f"\nGENERATING {name} LINK")
                    f.write(f"\n{url}")
                f.close()
            f.close()
            os.remove(nomefile)
        else:
            holmes.Main.Menu(Mode)

    @staticmethod
    def Search(username, Mode):
        Mail_search.Banner(Mode)
        now = datetime.now()
        dataformat = DateFormat.Get.Format()
        dt_string = now.strftime(dataformat)
        Date = f"Date: {str(dt_string)}"
        report = f"GUI/Reports/E-Mail/{username}.txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        with open(report, "w") as f:
            f.write("SCANNING EXECUTED ON:\n" + Date + "\n")
        mail.Validator.Mail(username, report)
        Mail_search.searcher(username, report, Mode)
        Mail_search.Lookup(username, report)
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Mail_search.Google_dork(username)
            Mail_search.Yandex_dork(username)
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
              os.getcwd() + "/" + report)
        with open(report, "a") as f:
            f.write(Language.Translation.Translate_Language(
                filename, "Report", "Default", "By"))
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
              report)
        Notification.Notifier.Start(Mode)
        Creds.Sender.mail(report, username)
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Transfer", "Question", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            FileTransfer.Transfer.File(report, username, ".txt")
        Encoding.Encoder.Encode(report)
        inp = input(Language.Translation.Translate_Language(
            filename, "Default", "Continue", "None"))
