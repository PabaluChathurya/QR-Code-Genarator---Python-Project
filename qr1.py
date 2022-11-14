import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Coding With Pabalu")
qr.png("myCode.png", scale=8)

d = decode(Image.open("mycode.png"))
print(d[0].data.decode("Ascii"))