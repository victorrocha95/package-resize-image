from PIL import Image

def executar():
    img = Image.open('logo.png') 
    height = img.size[0] 
    width = img.size[1] 
    print('Ratio before conversion:', width/height) 
    width = width + 25
    height = height - 25
    img = img.resize((width ,height), Image.ANTIALIAS) 
    print('Ratio after conversion:', width/height) 
    img.save('Resized Image.png')