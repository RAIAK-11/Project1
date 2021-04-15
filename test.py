import cv2
from skimage import io
import numpy as np
img = cv2.imread(r"eren.png",1)
#img3=img3.astype(np.float64)/255
io.imshow("https://d3nn873nee648n.cloudfront.net/900x600/19494/220-SM927611.jpg")
io.show()
#cv2.imshow("CUte jittens",img)
l=list()
for i in range(500):
    l.append(img[i])
l.reverse()
img2=np.array(l)
#cv2.imshow("CUte jittens",img2)
for i in range(0,499):
    t=img[i]
    img[i]=img[499-i]
    img[499-i]=t

