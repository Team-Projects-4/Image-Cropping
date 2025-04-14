from PIL import Image
import sys
import time
import os
margin = 30
backgroundColor = (121, 166, 210, 255)
def removeBackground(image: Image, dim):
    pixels = image.load()
    width, height = dim
    for y in range(height):
        redBorders = [] #holds the indexes of the borders
        prevPixelRed = False
        currentPixelRed = False
        for x in range(width):
            r,g,b, _ = pixels[x, y]
            currentPixelRed = r > 255 - margin and g < margin and b < margin #red found
            if currentPixelRed != prevPixelRed or (currentPixelRed and x == width - 1):
                redBorders.append(x) #new border found
            prevPixelRed = currentPixelRed
        #print("redborders: " + str(redBorders))
        for i in range(redBorders[0]):
            pixels[i, y] = backgroundColor
        for i in range(redBorders[-1], width):
            if redBorders[-1] != width -1: #ignore trimming the last index
                pixels[i, y] = backgroundColor
    return image
def main():
    testMode = False
    if len(sys.argv) == 2:
        if sys.argv[1] == "-t":
            testMode = True
            print("running in test mode!")
        else:
            print("Unknown argument: \"" + sys.argv[1] + "\"")
            return
    if testMode:
        inputDirectory = "/home/team4/repos/Image-Cropping/testing/"
    else:
        inputDirectory = "/home/team4/repos/Image-Cropping/input/"
    outputDirectory = "/home/team4/repos/Image-Cropping/output/"
    #make new directory if needed:
    os.makedirs(inputDirectory, exist_ok=True)
    fileNames = []
    #get all files in the directory:
    for filename in os.listdir(inputDirectory):
        filepath = os.path.join(inputDirectory, filename)
        if os.path.isfile(filepath) and filename[-4:] == ".png":
            #removes the .png file extension
            fileNames.append(filename[:-4])
    if (len(fileNames) == 0):
        print("No png files found in \"" + inputDirectory + "\"")
        if not testMode:
            print("Recommendation: Run with \'-t\' flag to run in test mode!")
        return
    os.makedirs(outputDirectory, exist_ok=True)
    #change margin for tighter or more relaxed qualifying pixels
    i = 0
    for imgName in fileNames:
        i = i + 1
        #for measuring time it takes to run
        #print("starting on image: " + imgName + ".png")
        startTime = time.time()
        img = Image.open(inputDirectory + imgName + ".png")
        width, height = img.size
        pixels = img.load()
        minX = width
        maxX = 0
        minY = height
        maxY = 0
        #iterate through each pixel...
        #get the circle edges:
        for y in range(height):
            for x in range(width):
                #compare RGB values:
                r, g, b, _ = pixels[x,y]
                if (r >= 255 - margin and g <= margin and b <= margin):
                    minX = min(minX, x)
                    maxX = max(maxX, x)
                    minY = min(minY, y)
                    maxY = max(maxY, y)
        #crop image
        if minX < maxX and minY < maxY:  # Ensure valid crop area
            pass
        else:
            print("No red area found in image: " + inputDirectory + imgName + ".png")
            print("Recommendation: Try adjusting the margin!")
            return

        #left, upper, right, lower
        croparea = (minX, minY, maxX, maxY)
        dimensions = (maxX - minX, maxY - minY)
        croppedImg = img.crop(croparea)
        #save image
        fullyCropppedImg = removeBackground(croppedImg, dimensions)
        fullyCropppedImg.save("image" + str(i) + ".png")
        #croppedImg.save(outputDirectory + imgName + "-cropped.png")
        endTime = time.time()
        totalTime = endTime - startTime
        print("image cropped: \"" + outputDirectory + imgName + "\"\t", end="")
        print(f"Task completed in {totalTime:.3f} seconds")
    
    

if __name__ == "__main__":
    main()
