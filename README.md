# Image-Cropping
### Project to crop the red circled area in the Death Star image


# Instructions:
1. put raw .png images into the "input" directory
2. run ```python3 image_crop.py```
3. all images will appear cropped in the "output" directory

# Testing:
1. testing images are included in the "testing" directory
2. run the same command with "-t" at the end to run in "test mode"
3. ```python3 image_crop.py -t```
4. this will generate the cropped images and place them in the "output" directory.

# Notes:
1. "margin" is set to 30 by default, change this to adjust the qualifying margin. The qualifying margin determines how far away from red (RGB = 255, 0, 0) a qualifying pixel can be.
2. Background color can also be changed to another color value.
3. All cropped images will appear in the "output" directory with "-cropped.png" appended to the image name.