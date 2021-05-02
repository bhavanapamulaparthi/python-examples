import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=8,
    border=5
)

str = "hello i am bhavana"
qr.add_data(str)
qr.make(fit=True)
img = qr.make_image(fill="white", back_color="blue")
img.save("qr2.png")