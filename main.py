# main function
"""

"""

from PIL import Image
import time

from loggingAndOutput import Logging
from generateAndPopulate import GenerateAndPopulate
Logging = Logging(False)

from creation import Creation
from statics import materials

# user input for name and image size
def imageInfo(newCreation):
    # assemble the options for materials it can be built out of
    materialOptions = []
    for i in materials:
        if "Wall" in i:
            materialOptions.append(i.strip("Wall"))

    try:
        imgName =       "mapX" #input("please enter image name")
        blocksHeight =  int(input("please enter the number of 5x5 blocks tall (less than 20 is recommended for performance)"))
        blocksWidth =   int(input("please enter the number of 5x5 blocks wide (less than 20 is recommended for performance)"))
        generationIterations = int(input('please enter the number of map-cycle iterations (1-3 is plenty)'))
        material =          input(f"please enter the material wanted from \x1b[3m \033[1;33;48m{materialOptions}\033[0m")
        pixelsPerBlock =    int(input('please enter the number of pixels per 5x5 block'))
        continuousBorders = bool(input('would you like the borders to be continuous?\x1b[3m \033[1;33;48m["True", "False"]\033[0m)'))

    except Exception as e:
        imgName = "map"
        blocksWidth = 120
        blocksHeight = 90
        generationIterations = 2
        pixelsPerBlock = 50
        continuousBorders = True
        material = 'wood'
        Logging.error(f"improper input given. Defaulting to:\n "
                      f"{blocksWidth} blocks wide\n "
                      f"{blocksHeight} blocks tall\n "
                      f"{generationIterations} iterations run for map generation \n"
                      f"{material} material \n"
                      f"{pixelsPerBlock} pixels per plock \n"
                      f"{continuousBorders} continuous borders \n"
                      f"exception thrown: {e}")


    imgHeight = blocksHeight*pixelsPerBlock
    imgWidth = blocksWidth*pixelsPerBlock

    Logging.say(f"Configuration for map:\n"
                f" number of blocks wide: {blocksWidth} \n "
                f" number of blocks tall: {blocksHeight} \n "
                f" number of iterations run for map generation: {generationIterations}  \n"
                f" background material for the map: {material}  \n"
                f" number of pixels per plock: {pixelsPerBlock}  \n"
                f" continuous borders: {continuousBorders}  \n")

    newCreation.blockSize = min(round(imgHeight/blocksHeight), round(imgWidth/blocksWidth) )
    newCreation.blocksHeight = blocksHeight
    newCreation.blocksWidth = blocksWidth
    newCreation.imgName = imgName
    newCreation.imgWidth = imgWidth
    newCreation.imgHeight = imgHeight
    newCreation.generationIterations = generationIterations
    newCreation.material = material
    newCreation.continuousBorders = continuousBorders

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
