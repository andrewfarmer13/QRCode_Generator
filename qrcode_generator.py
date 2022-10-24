# -*- coding: utf-8 -*-
"""
@author: andrew
"""

import qrcode

url = input("Enter the Url that you wish to convert to a qr code: ")
name = input("What do you want to name the qr_code: ")

qr = qrcode.make(url)

qr.save(name + ".png")

