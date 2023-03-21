# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import phonenumbers
import MrHolmes as holmes
import json
import urllib
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from Core.Support import Font
from Core.Support import Language
from Core.Support import Map
from time import sleep

filename = Language.Translation.Get_Language()
filename


class Phony:

    @staticmethod
    def Get_GeoLocation(zone, param1, param2, jsonfile, num, Type):
        req = f"https://nominatim.openstreetmap.org/search.php?q={zone}&format=json"
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Phone", "Geo", "None").format(num))
        sleep(2)
        url = urllib.request.urlopen(req)
        try:
            Reader = url.read()
            parser = json.loads(Reader)
            Lat = parser[0]["lat"]
            Lon = parser[0]["lon"]
            data = {
                "Geolocation": {
                    "Latitude": Lat,
                    "Longitude": Lon
                }
            }
            print(
                (
                    f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}LATITUDE:{Font.Color.GREEN}"
                    + f" {Lat}"
                )
            )
            sleep(2)
            print(
                (
                    f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}LONGITUDE:{Font.Color.GREEN}"
                    + f" {Lon}"
                )
            )
            sleep(2)
            print(
                (
                    f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}"
                    + f"GOOGLE MAPS LINK: https://www.google.it/maps/place/{Lat},{Lon}"
                )
            )
            with open(jsonfile, "a", encoding="utf-8") as datafile:
                json.dump(data, datafile,
                          ensure_ascii=False, indent=4)
            Map.Creation.mapPhone(jsonfile, Lat, Lon, num, Type)

        except Exception as e:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Phone", "NoGeo", "None") + str(e))

    @staticmethod
    def Number(num, report, code, Mode, Type, username):
        print(Font.Color.GREEN +
              "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Phone", "Scan", "None").format(num))
        sleep(4)
        FormattedPhoneNumber = f"+{num}"
        try:
            Phone = phonenumbers.parse(FormattedPhoneNumber, None)
        except Exception as e:
            inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                        Language.Translation.Translate_Language(filename, "Phone", "NotFound2", "None"))
            holmes.Main.Menu(Mode)
        else:
            if not phonenumbers.is_valid_number(Phone):
                reality = (Language.Translation.Translate_Language(
                    filename, "Phone", "NoReal", "None"))
            else:
                reality = Language.Translation.Translate_Language(
                    filename, "Phone", "Real", "None")
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + reality)

            number = phonenumbers.format_number(
                Phone, phonenumbers.PhoneNumberFormat.E164
            ).replace("+", "")
            numberCode = phonenumbers.format_number(
                Phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            ).split(" ")[0]
            numberNation = phonenumbers.region_code_for_country_code(
                int(numberCode)
            )

            localNumber = phonenumbers.format_number(
                Phone, phonenumbers.PhoneNumberFormat.E164
            ).replace(numberCode, "")
            international = phonenumbers.format_number(
                Phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )

            nation = geocoder.country_name_for_number(Phone, "en")
            location = geocoder.description_for_number(Phone, "en")
            carrierName = carrier.name_for_number(Phone, "en")

            print(
                (
                    Font.Color.YELLOW
                    + "\n[v]"
                    + Font.Color.WHITE
                    + f"INTERNATIONAL NUMBER: {international}"
                )
            )
            print(
                (
                    Font.Color.YELLOW
                    + "[v]"
                    + Font.Color.WHITE
                    + f"LOCAL NUMBER: {localNumber}"
                )
            )
            print(
                (
                    f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}"
                    + f"COUNTRY PREFIX: {numberCode}"
                )
            )
            print(
                (
                    f"{Font.Color.YELLOW}[v]{Font.Color.WHITE}"
                    + f"COUNTRY CODE: {numberNation}"
                )
            )
            print(
                (
                    Font.Color.YELLOW
                    + "[v]"
                    + Font.Color.WHITE
                    + f"COUNTRY: {nation}"
                )
            )
            print(
                (
                    Font.Color.YELLOW
                    + "[v]"
                    + Font.Color.WHITE
                    + f"AREA/ZONE: {location}"
                )
            )
            print(
                (
                    Font.Color.YELLOW
                    + "[v]"
                    + Font.Color.WHITE
                    + f"CARRIER/ISP: {carrierName}"
                )
            )
            i = 1
            for timezoneResult in timezone.time_zones_for_number(Phone):
                print(
                    (
                        Font.Color.YELLOW
                        + "[v]"
                        + Font.Color.WHITE
                        + f"TIMEZONE N°{i}: {timezoneResult}"
                    )
                )
                i = i+1
            sleep(2)
            if location != "":
                jsonfile = report.replace(f"{num}.txt", "Area_GeoLocation.json")
                zone = location.split(" ", 1)[1] if " " in location else location
                print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "Area", "None"))
                Phony.Get_GeoLocation(zone, "Lat", "Long", jsonfile, num, Type)
            else:
                print(
                    (
                        f"{Font.Color.RED}[!]{Font.Color.WHITE}"
                        + Language.Translation.Translate_Language(
                            filename, "Phone", "NoArea", "None"
                        )
                    )
                )
            zone = timezoneResult.split("/", 1)[-1]

            if zone != "Unknown":
                print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "Zone", "None"))
                jsonfile = report.replace(f"{num}.txt", "Zone_GeoLocation.json")
                Phony.Get_GeoLocation(zone, "Lat", "Long", jsonfile, num, Type)

            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "NoZone", "None").format(number))
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Phone", "Affidability", "None"))
            sleep(2)
            if phonenumbers.is_possible_number(Phone):
                print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "Exist", "None"))
            else:
                print(Font.Color.RED +
                      "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Phone", "NoExist", "None"))

            with open(report, "a") as f:
                f.write(f"INTERNATIONAL NUMBER: {international}" + "\n")
                f.write(f"LOCAL NUMBER: {localNumber}" + "\n")
                f.write(f"COUNTRY PREFIX: {numberCode}" + "\n")
                f.write(f"COUNTRY CODE: {numberNation}" + "\n")
                f.write(f"COUNTRY:{nation}" + "\n")
                f.write(f"AREA/ZONE{location}" + "\n")
                f.write(f"CARRIER/ISP: {carrierName}" + "\n")
                f.write(f"TIMEZONE: {timezoneResult}" + "\n")
            if code == 0:
                pass
            elif code == 1:
                with open("Temp/Phone/Code.txt", "w") as f:
                    f.write(numberNation)
