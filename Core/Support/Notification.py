# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os

class Notifier:

    @staticmethod
    def Start(Mode):
        if Mode == "Desktop" and os.name != "nt":
            os.system("java Core/Support/Notification/Notification.java")