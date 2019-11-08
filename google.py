from PIL import Image

def images():
    accepted = False
    while not accepted:
        try:
            f = input("Need inspiration... input filename in images folder: ")
            img = Image.open("images/%s"%f)
            accepted = True
        except:
            print("Invalid file, Try Again")
    img = img.convert("HSV")
    pix = img.load()
    return pix

