import qrcode

class main:
    print("Add some data to generate qr code.")
    data = input("?")
    image = qrcode.make(data)
    image.save("qrcode.png")
    image.show()
