import qrcode # first install the models => pip install qrcode[pil]   

data = input(" Enter text or URL to generate QR code: ")

qr = qrcode.make(data)

file_name = "qrcode.png"

qr.save(file_name)

print(f"QR Code generated and saved as {file_name} ")
