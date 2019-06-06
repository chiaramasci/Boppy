import webcolors
import pygame
import pygame.freetype
import sys
import envirophat
from time import sleep
import board
import neopixel
from matplotlib import colors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    rgb = (0,0,0)
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        rgb = colors.to_rgb(closest_name)
        red = int(rgb[0] * 100)
        green = int(rgb[1] * 100)
        blue = int(rgb[2] * 100)
        rgb = (red, green, blue)
    return rgb, closest_name

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
        
X = 800
Y = 800
pixel_pin = board.D18
num_pixels = 16
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False,pixel_order=ORDER)
rainbow_cycle(0.001)


sleep(1)
colornoise = envirophat.light.rgb()#
print("Cal complete")

pygame.init()
pygame.font.init()
pygame.display.set_caption('Boppy')

rainbow_cycle(0.001)
while True:
    print(colornoise)
    screen = pygame.display.set_mode((1000,600))
    background = (241, 254, 255)
    screen.fill((background))
    font1 = pygame.freetype.SysFont("Vegan Style Personal Use", 55)
    text = font1.render_to(screen, (X // 2, 0), "Boppy!", (0,0,0))
    pygame.display.update()
    sleep(4)
    requested_colour = envirophat.light.rgb()
    calred = requested_colour[0] - colornoise[0]
    calgreen = requested_colour[1] - colornoise[1]
    calblue = requested_colour[2] - colornoise[2]
    calcolor = (calred, calgreen, calblue)
    rgb, closest_name = get_colour_name(calcolor)
    print ("Actual colour name:", rgb, ", closest colour name:", closest_name)
    background = rgb
    screen.fill((background))
    pixels.fill((rgb))
    pixels.show()
    pygame.display.update()
