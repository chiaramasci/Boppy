from picamera import PiCamera
from time import sleep
from PIL import Image


camera = PiCamera()
camera.start_preview()
sleep(3)
camera.capture('image.jpg')
camera.stop_preview()

img = Image.open("image.jpg")

def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel[1]

color = most_frequent_colour(img)
