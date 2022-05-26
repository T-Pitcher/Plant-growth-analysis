#Status: Works 2022-04-30
#counts the coloured pixels in an image within set R, G, B thresholds
#and outputs a b/w image in output folder

from PIL import Image

newimage2 = Image.open("12colours.png")
pix = newimage2.load()
#print(newimage2.size)
totalpix = newimage2.width * newimage2.height

RedMaxThreshold = 100
RedMinThreshold = 0

GreenMaxThreshold = 100
GreenMinThreshold = 0

BlueMaxThreshold = 100
BlueMinThreshold = 0


selectedValues = 0
x = 0
while x < newimage2.width:
    y = 0
    while y < newimage2.height:
        if (pix[x,y][0] <= RedMaxThreshold and pix[x,y][0] >= RedMinThreshold
        and pix[x,y][1] <= GreenMaxThreshold and pix[x,y][1] >= GreenMinThreshold
        and pix[x,y][2] <= BlueMaxThreshold and pix[x,y][2] >= BlueMinThreshold):
                selectedValues = selectedValues + 1
                pix[x,y] = (0, 0, 0)
        else:
            pix[x,y]= (255, 255, 255)
        y = y+1
    x = x+1

percentSelected = round((100*selectedValues/totalpix), 2)
#print(newimage2.filename)
print(str(percentSelected) +" % within spec")

topcorner = pix[0,0]
#print(topcorner)

import os
'''if not os.path.isdir("output"):
    #os.rmdir("output")
    os.mkdir("output")'''

from shutil import rmtree
rmtree("output")
os.mkdir("output")

savename = "output/" + str(newimage2.filename) + "_output"+ ".png"
newimage2.save(savename)

newimage2.close()
#print(pix[0,0][0])

# python pixcount_while_colour_w_output.py
