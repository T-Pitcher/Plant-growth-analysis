#Status: Works
#takes a RGNIR image and outputs a greyscale or colour coded image
# with 5 or 10 bands for all images in \NIRinput folder
#can be equal spacing or equal area
# python pixchange_for_NDVI_3_multi.py

from PIL import Image
from time import time
import glob
import os

start = time()

#Settings:
From_RGNIR = True
Equal_area = True
To_Colourbands = True
Print_cutoffs = True
Band_No = 10
#Band_No either 5 or 10

if not os.path.isdir("NIRoutput"):
    #os.rmdir("output")
    os.mkdir("NIRoutput")

paths = glob.glob("NIRinput\*.png")
for path in paths:
    newimage2 = Image.open(path)
    #newimage2 = Image.open("Wheat-FW00051corrected.png")
    pix = newimage2.load()
    #print(newimage2.size)
    #totalpix = newimage2.width * newimage2.height
    #print(pix[0,0])

    #convert RGNIR to RGB:
    if From_RGNIR:
        for x in range(newimage2.width):
            for y in range(newimage2.height):
                try: NDVI = (pix[x, y][2]-pix[x, y][0])/(pix[x, y][2]+pix[x, y][0])
                except:NDVI = 0
                NDVI = 255*(NDVI+1)/2
                NDVI = int(NDVI)
                pix[x, y] = (NDVI, NDVI, NDVI)

    #Set bands:
    class Band:
        min=0
        max=0
        r=0
        g=0
        b=0
        def __init__(self, min, max, r, g, b):
            self.min = min
            self.max = max
            self.r = r
            self.g = g
            self.b = b

    if Band_No == 5:
        b1 = Band(0, 51, 215, 25, 28)
        b2 = Band(51, 102, 233, 140, 14)
        b3 = Band(102, 153, 251, 255, 1)
        b4 = Band(153, 204, 139, 203, 33)
        b5 = Band(204, 256, 26, 150, 65)
        b6 = Band(256, 256, 0,0,0)
        b7 = Band(256, 256, 0,0,0)
        b8 = Band(256, 256, 0,0,0)
        b9 = Band(256, 256, 0,0,0)
        b10 = Band(256, 256, 0,0,0)
    elif Band_No == 10:
        b1 = Band(0, int(255/Band_No), 215, 25, 28)
        b2 = Band(b1.max, int(2*(255/Band_No)), 224, 89, 25)
        b3 = Band(b2.max, int(3*(255/Band_No)), 232, 130, 17)
        b4 = Band(b3.max, int(4*(255/Band_No)), 241, 179, 11)
        b5 = Band(b4.max, int(5*(255/Band_No)), 249, 230, 5)
        b6 = Band(b5.max, int(6*(255/Band_No)), 226, 243, 14)
        b7 = Band(b6.max, int(7*(255/Band_No)), 177, 220, 28)
        b8 = Band(b7.max, int(8*(255/Band_No)), 129, 197, 39)
        b9 = Band(b8.max, int(9*(255/Band_No)), 87, 173, 55)
        b10 = Band(b9.max, int(256), 26, 150, 65)

    print("time:" + str(time() - start))
    #Set band widths for equal area:
    if Equal_area:
        valueslist = list(newimage2.getdata(0))
        #b1.min = 0
        b1.min = 0
        b1.max = min(valueslist)

        Band_Width = len(valueslist)/Band_No

        valuefreq = newimage2.histogram()
        cumulativePix = 0
        #print(valuefreq)
        n = min(valueslist)
        while cumulativePix < Band_Width*1:
            cumulativePix+=valuefreq[n]
            n+=1
            b1.max = n
        #print(cumulativePix)

        while cumulativePix < Band_Width*2:
            cumulativePix+=valuefreq[n]
            n+=1
            b2.max = n

        while cumulativePix < Band_Width*3:
            cumulativePix+=valuefreq[n]
            n+=1
            b3.max = n
        #print(cumulativePix)

        while cumulativePix < Band_Width*4:
            cumulativePix+=valuefreq[n]
            n+=1
            b4.max = n

        while cumulativePix < Band_Width*5:
            cumulativePix+=valuefreq[n]
            n+=1
            b5.max = n

        while cumulativePix < Band_Width*6:
            cumulativePix+=valuefreq[n]
            n+=1
            b6.max = n

        while cumulativePix < Band_Width*7:
            cumulativePix+=valuefreq[n]
            n+=1
            b7.max = n

        while cumulativePix < Band_Width*8:
            cumulativePix+=valuefreq[n]
            n+=1
            b8.max = n

        while cumulativePix < Band_Width*9:
            cumulativePix+=valuefreq[n]
            n+=1
            b9.max = n

        while cumulativePix < Band_Width*10:
            cumulativePix+=valuefreq[n]
            n+=1
            b10.max = n


        #print(cumulativePix)

        b2.min = b1.max
        b3.min = b2.max
        b4.min = b3.max
        b5.min = b4.max

        b6.min = b5.max
        b7.min = b6.max
        b8.min = b7.max
        b9.min = b8.max
        b10.min = b9.max

    if Print_cutoffs:
        print(" ")
        print(b1.max)
        print(b2.max)
        print(b3.max)
        print(b4.max)
        print(b5.max)

        print(b6.max)
        print(b7.max)
        print(b8.max)
        print(b9.max)
        print(b10.max)

        print(" ")
        print((b1.min/127.5)-1)
        print((b1.max/127.5)-1)
        print((b2.max/127.5)-1)
        print((b3.max/127.5)-1)
        print((b4.max/127.5)-1)

        print((b5.max/127.5)-1)
        print((b6.max/127.5)-1)
        print((b7.max/127.5)-1)
        print((b8.max/127.5)-1)
        print((b9.max/127.5)-1)
        print((b10.max/127.5)-1)

    print("time:" + str(time() - start))

    #convert to colour bands
    if To_Colourbands:
        for x in range(newimage2.width):
            for y in range(newimage2.height):
                if (pix[x, y][0] >= b1.min and pix[x, y][0]< b1.max):
                    pix[x, y] = (b1.r, b1.g, b1.b)
                elif (pix[x, y][0] >= b2.min and pix[x, y][0]< b2.max):
                    pix[x, y] = (b2.r, b2.g, b2.b)
                elif (pix[x, y][0] >= b3.min and pix[x, y][0]< b3.max):
                    pix[x, y] = (b3.r, b3.g, b3.b)
                elif (pix[x, y][0] >= b4.min and pix[x, y][0]< b4.max):
                    pix[x, y] = (b4.r, b4.g, b4.b)
                elif (pix[x, y][0] >= b5.min and pix[x, y][0]< b5.max):
                    pix[x, y] = (b5.r, b5.g, b5.b)
                elif (pix[x, y][0] >= b6.min and pix[x, y][0]< b6.max):
                    pix[x, y] = (b6.r, b6.g, b6.b)
                elif (pix[x, y][0] >= b7.min and pix[x, y][0]< b7.max):
                    pix[x, y] = (b7.r, b7.g, b7.b)
                elif (pix[x, y][0] >= b8.min and pix[x, y][0]< b8.max):
                    pix[x, y] = (b8.r, b8.g, b8.b)
                elif (pix[x, y][0] >= b9.min and pix[x, y][0]< b9.max):
                    pix[x, y] = (b9.r, b9.g, b9.b)
                elif (pix[x, y][0] >= b10.min and pix[x, y][0]< b10.max):
                    pix[x, y] = (b10.r, b10.g, b10.b)
                else:
                    pix[x, y]= (255, 255, 255)

    #Save output:
    #import os
    #from shutil import rmtree
    #try: rmtree("output2")
    #os.mkdir("output2")

    filename = os.path.basename(path)
    savename = "NIRoutput/" + str(filename) + "_output"+ ".png"
    newimage2.save(savename)

    #newimage2.show()
    newimage2.close()

    print("time:" + str(time() - start))

print("time:" + str(time() - start))
print(" ")

# python pixchange_for_NDVI_3_multi.py
