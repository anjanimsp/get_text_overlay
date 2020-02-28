import cv2
import numpy as np

def getTextOverlay(input_image):
    con_green=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);plt.imshow(con_green)
    _,thresh= cv2.threshold(con_green,3,255,cv2.THRESH_BINARY)
    thresh=cv2.cvtColor(thresh,cv2.COLOR_GRAY2RGB)
    mask=cv2.multiply(img,thresh)
    
    return mask
    
     
    # Write your code here for output
    
    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
