import webcolors
from PIL import Image
from time import sleep
import board
import neopixel
from picamera import PiCamera
from requests import get

url ='http://10.7.104.110:5000/'

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        sleep(wait)

def most_frequent_colour(image):
    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel[1]
        
X = 800
Y = 800
camera = PiCamera()
pixel_pin = board.D18
num_pixels = 16
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False,pixel_order=ORDER)

rainbow_cycle(0.0001)
while True:
    camera.start_preview()
    sleep(2)
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    print("Taking pic...")
    camera.capture('image.jpg')
    camera.stop_preview()
    print("Analyzing...")
    img = Image.open("image.jpg")
    img = img.resize((200,200))

    rgb = most_frequent_colour(img)
    #response = get(url+"pink")

    print ("Actual colour name:", rgb)
    pixels.fill((rgb))
    pixels.show()
