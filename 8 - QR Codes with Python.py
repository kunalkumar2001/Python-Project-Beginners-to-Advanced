import qrcode


url = input("Enter the URL to generate QR Code: ").strip()

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.show()