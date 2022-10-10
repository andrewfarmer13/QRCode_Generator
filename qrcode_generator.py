# -*- coding: utf-8 -*-
"""
@author: andrew
"""

import qrcode

url = input("Enter the Url that you wish to convert to a qr code: ")

qr = qrcode.make(url)

qr.save("my_qr.png")

