from PIL import Image
import sys
import os
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
        inputDirectory = "testing/"
    else:
        inputDirectory = "input/"
    outputDirectory = "output/"
    #make new directory if needed:
    fileNames = []
    #get all files in the directory:
    for filename in os.listdir(inputDirectory):
        filepath = os.path.join(inputDirectory, filename)
        if os.path.isfile(filepath) and filename[-4:] == ".png":
            #removes the .png file extension
            fileNames.append(filename[:-4])
    if (len(fileNames) == 0):
        print("No png files found in \"./" + inputDirectory + "\"")
        if not testMode:
            print("Recommendation: Run with \'-t\' flag to run in test mode!")
        return
    os.makedirs(outputDirectory, exist_ok=True)
    #change margin for tighter or more relaxed qualifying pixels
    margin = 25
    for imgName in fileNames:
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
                r, g, b, a = pixels[x,y]
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
        croppedImg = img.crop(croparea)
        #save image
        croppedImg.save(outputDirectory + imgName + "-cropped.png")
    
    

if __name__ == "__main__":
    main()
