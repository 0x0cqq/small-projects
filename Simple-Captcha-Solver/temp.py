# 将透明底换成白色底
from PIL import Image
import numpy as np

np.set_printoptions(threshold=np.inf)


if __name__ == "__main__":
    for num in range(10):
        num_img = Image.open("nums-alpha/" + str(num) + ".png")
        for i in range(0,num_img.size[0]):
            for j in range(0,num_img.size[1]):
                p = num_img.getpixel((i,j)) 
                if(p[3] == 0):
                    p = (255,255,255,255)
                num_img.putpixel((i,j),p)
        num_img.save(str(num) + ".png","PNG")
        num_img.show()
    pass