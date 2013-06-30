from PIL import Image
import random
from bisect import bisect

zone=[36,72,108,144,180,216,252]

greyness = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)",
            "mdK4ZGbN",
            "W8KMA",
            "#%$"
            ]


 
pic=Image.open("") #Insert the location of the image here
pic=pic.resize((200, 100),Image.BILINEAR)
pic=pic.convert("L") # convert to mono
 
str=""
for y in range(0,pic.size[1]):
    for x in range(0,pic.size[0]):
        glow=255-pic.getpixel((x,y))
        row=bisect(zone,glow)
        possibles=greyness[row]
        str=str+possibles[random.randint(0,len(possibles)-1)]
    str=str+"\n"
 
fo = open("", "wb")#Insert the destination of the ".txt" file here!
fo.write(str);

fo.close()
