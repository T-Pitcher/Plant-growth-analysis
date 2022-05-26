#python Green_Count_Median_Colour.py
#Status: Works but slow 2022-05-09
'''counts the coloured pixels in an image within set R, G, B thresholds
and makes a csv file of area fraction and average colour of selected pixels
optional: outputs a b/w image in output folder (deletes previous output folder)
'''
from PIL import Image
import glob
import os
'''
if not os.path.isdir("output"):
    #os.rmdir("output")
    os.mkdir("output")


from shutil import rmtree
rmtree("output")
os.mkdir("output")
'''

MaxThreshold0 = 130
MinThreshold0 = 30

MaxThreshold1 = 255
MinThreshold1 = 100

MaxThreshold2 = 255
MinThreshold2 = 50

#length in pixels of 30 cm ruler
#rulerLen = 1157
#convert pixels to cm**2
#cm_per_px = 30/1157
cm2_per_px = (30/1157)**2

#CSV setup
CSV_headers = ['File name', 'Green Pixels', 'Green area (cm2)', 'Median Hue', 'Median Sat', 'Median Val']
CSV_rows = []



paths = glob.glob("*.jpg")
for path in paths:
    photo = Image.open(path)
    photo.convert('HSV')
    pix = photo.load()
    #print(photo.size)
    totalpix = photo.width * photo.height
    selectedValues = 0
    Colours0 = []
    Colours1 = []
    Colours2 = []

    for x in range(photo.width):
        for y in range(photo.height):
            if (pix[x,y][0] <= MaxThreshold0 and pix[x,y][0] >= MinThreshold0
            and pix[x,y][1] <= MaxThreshold1 and pix[x,y][1] >= MinThreshold1
            and pix[x,y][2] <= MaxThreshold2 and pix[x,y][2] >= MinThreshold2):
                    selectedValues = selectedValues + 1
                    #pix[x,y]= (0,0,0)
                    Colours0.append(pix[x,y][0])
                    Colours1.append(pix[x,y][1])
                    Colours2.append(pix[x,y][2])
            #else:
            #    pix[x,y]= (255, 255, 255)

    #percentSelected = round((100*selectedValues/totalpix), 2)
    Total_cm2 = selectedValues*cm2_per_px
    SortedColours0 = Colours0.sort()
    Median0 = Colours0[int(len(Colours0)/2)]
    #Mean0 = sum(Colours0)/ len(Colours0)

    SortedColours1 = Colours1.sort()
    Median1 = Colours1[int(len(Colours1)/2)]

    SortedColours2 = Colours2.sort()
    Median2 = Colours2[int(len(Colours2)/2)]
    CSV_rows.append([photo.filename, selectedValues, Total_cm2, Median0, Median1, Median2])
    #print(str(photo.filename) + ': ' +  str(percentSelected) +" % within spec")

    #savename = "output/" + str(photo.filename) + "_output"+ ".png"
    #photo.save(savename)
    photo.close()

import csv
filename = 'Green Analysis.csv'
with open(filename, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(CSV_headers)
    csvwriter.writerows(CSV_rows)

# python ..\Green_Count_Median_Colour.py
