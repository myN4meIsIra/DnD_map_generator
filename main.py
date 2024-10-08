#
"""

"""

from PIL import Image
import time
import random

from element import Element
from building_rules import rules
from loggingAndOutput import Logging
from generateAndPopulate import GenerateAndPopulate
Logging = Logging(False)

from creation import Creation


# user input for name and image size
def imageInfo(newCreation):
    try:
        imgName =       "mapX" #input("please enter image name")
        blocksHeight =  int(input("please enter the number of 5x5 blocks tall"))
        blocksWidth =   int(input("please enter the number of 5x5 blocks wide"))
        generationIterations = int(input('please enter the number of map-cycle iterations'))
        material =          input("please enter the material wanted")
        #imgHeight =     int(input("please enter image height"))
        #imgWidth =      int(input("please enter image width"))
    except Exception as e:
        imgName = "map"
        blocksWidth = 120
        blocksHeight = 90
        generationIterations = 2
        material = 'wood'
        Logging.error(f"improper input given. Defaulting to:\n "
                      f"{blocksWidth} blocks wide\n "
                      f"{blocksHeight} blocks tall\n "
                      f"{generationIterations} iterations \n"
                      f"{material} material \n"
                      f"exception thrown: {e}")


    imgHeight = blocksHeight*50
    imgWidth = blocksWidth*50

    newCreation.blockSize = min(round(imgHeight/blocksHeight), round(imgWidth/blocksWidth) )
    newCreation.blocksHeight = blocksHeight
    newCreation.blocksWidth = blocksWidth
    newCreation.imgName = imgName
    newCreation.imgWidth = imgWidth
    newCreation.imgHeight = imgHeight
    newCreation.generationIterations = generationIterations
    newCreation.material = material

    return 1


# main function
def main():
    # create instace of creation class
    newCreation = Creation()

    # get image base info
    imageInfo(newCreation)

    imgName = newCreation.imgName
    imgWidth = newCreation.imgWidth
    imgHeight = newCreation.imgHeight
    generationIterations = newCreation.generationIterations
    material = newCreation.material

    img = Image.new("RGB", (imgWidth, imgHeight), "black")  # Create a new black image
    pixels = img.load()  # Create the pixel map

    # image generation
    startTime = time.time()
    Logging.say("image creation started")
    generateAndPopulate = GenerateAndPopulate()
    img = generateAndPopulate.procedural_generation(newCreation, img, pixels, generationIterations, material)

    # stopwatch
    endTime = time.time()
    timeElapsed = endTime - startTime
    Logging.say(f"\nimage creation finished \n"
          f"time spent in generation: {round(timeElapsed // 60 // 60)}:{round(timeElapsed //60 % 60)}:{round(timeElapsed%60)}\t (hh:mm:ss)")

    # show then save the image
    img.show()
    img.save(f"{imgName}.png", "png")


    # https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
    # https://pillow.readthedocs.io/en/stable/reference/Image.html


if __name__ == '__main__':
    main()
