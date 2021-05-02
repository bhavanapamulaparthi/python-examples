# pip install pillow
# pip install pypng
# pip install pyzbar
# pip install pyqrcode

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("coding with bhavana")
qr.png("qrcode.png", scale=8)

d = decode(Image.open("qrcode.png"))
print(d)
print(d[0].data.decode("ascii"))