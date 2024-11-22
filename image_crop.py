from PIL import Image
import os
def main():
    inputDirectory = "input/"
    outputDirectory = "output/"
    #make new directory if needed:
    os.makedirs(outputDirectory, exist_ok=True)
    fileNames = []
    #get all files in the directory:
    for filename in os.listdir(inputDirectory):
        filepath = os.path.join(inputDirectory, filename)
        if os.path.isfile(filepath):
            #removes the .png file extension
            fileNames.append(filename[:-4])
    #change margin for tighter or more relaxed qualifying pixels
    margin = 30
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
                if (pixels[x, y][0] >= 255 - margin and pixels[x,y][1] <= margin and pixels[x,y][2] <= margin):
                    if (x > maxX):
                        maxX = x
                    if (x < minX):
                        minX = x
                    if (y > maxY):
                        maxY = y
                    if (y < minY):
                        minY = y
        #crop image
        #left, upper, right, lower
        croparea = (minX, minY, maxX, maxY)
        croppedImg = img.crop(croparea)
        #save image
        croppedImg.save(outputDirectory + imgName + "-cropped.png")
    
    

if __name__ == "__main__":
    main()
