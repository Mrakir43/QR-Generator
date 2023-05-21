import qrcode
img = qrcode.make(input('Please Type Here QR Body: \n'))
img.save(input("Please Type Here QR Name with .png: \n"))
img.show()