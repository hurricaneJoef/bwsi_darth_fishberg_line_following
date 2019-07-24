import cv2
#import imutils
import numpy as np
import pdb
low_range  = np.array([00, 220, 161])
high_range = np.array([28, 255, 255])
def cd_color_segmentation(img,color):
    

    low_range  = color[0]#np.array([00, 44, 147])
    high_range = color[1]#np.array([8, 254, 255])




    '''new_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(new_img, low_range, high_range)
    filtered = cv2.bitwise_and(new_img, img, mask=mask)
   cv2.imshow("filt",filtered)
	edges = cv2.Canny(mask,100,200)#
	#return mask
#hval
#red0-10
#blue 100-110
#yellow25-35
    '''


    '''
	Implement the cone detection using color segmentation algorithm
	    Input:
	    img: np.3darray; the input image with a cone to be detected
	Return:
	    bbox: ((x1, y1), (x2, y2)); the bounding box of the cone, unit in px
		    (x1, y1) is the bottom left of the bbox and (x2, y2) is the top right of the bbox
    '''

    
    # convert from rgb to hsv color space (it might be BGR)
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # define lower and upper bound of image values

    # create mask for image with overlapping values
    mask = cv2.inRange(new_img, low_range, high_range)
    #cv2.imshow(mask)
    # filter the image with bitwise and
    filtered = cv2.bitwise_and(new_img, img, mask=mask)

    # find the contours in the image
    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x1, y1, x2, y2 = 0, 0, 0, 0
    if len(contours) != 0:
	# find contour with max area, which is most likely the cone
        # Solution note: max uses an anonymous function in this case, we can also use a loop...
        contours_max = max(contours, key = cv2.contourArea)

	# Find bounding box coordinates
        x1, y1, x2, y2 = cv2.boundingRect(contours_max)

	# Draw the bounding rectangle
        cv2.rectangle(img, (x1, y1), (x1 + x2, y1 + y2), (0, 255, 0), 2)

    
    return (x1+x1+x2)/2
