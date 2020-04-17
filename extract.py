from PIL import Image
import pytesseract
import re
import cv2
import numpy as np
import os
# provide the cropped area with text

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def getLabel(tempFilepath, languages='eng'):
    img = tempFilepath
    text = pytesseract.image_to_string(img, lang=languages, config='--psm 6')
    final_text = ''
    #print("PT", text)
    text = text.split('\n')
    for i in range(len(text)):
    	final_text = final_text + text[i]

    ff = [char for char in final_text if char.isupper()]  # .join('')
    final_text = ''
    for i in range(0, len(ff)):
    	final_text = final_text + ff[i]

    print("text :{0}".format(final_text[:3]))

    return final_text[:3]


def getShelf(tempFilepath, languages='eng'):

	img = tempFilepath
	text = pytesseract.image_to_string(img, lang=languages ,config='--psm 8')
	#print("pytext",text)
	final_text =''
	#text = text.split('')
	# for i in range(len(text)):
	# 	final_text = final_text + text[i]
	# print(final_text)

	ff = [char for char in text if char.isupper()]  # .join('')
	final_text = ''
	#print("ff",ff)
	
	for i in range(0, len(ff)):
		final_text = final_text + ff[i]
	#print(final_text)
	
	final_text = final_text[0:3] + '-' + final_text[3:6]
	print ("text :{0}".format(final_text))

	return final_text

  
def getText(pil_image, target):

		# image1 = cv2.imread('./test_images/test'+str(i)+'.jpg')  
		open_cv_image = np.array(pil_image) 
		#image1 = cv2.cvtColor(open_cv_image,cv2.COLOR_RGB2BGR) #open_cv_image[:, :, ::-1].copy() 
		image1 = open_cv_image[:, :, ::-1].copy()
		#image1 = cv2.imread('./test_images/shelf.jpg')
		#print(image1.shape)
		  
		
		img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 
		height, width = img.shape
		
		if target == 'shelf':
			nh, nw = int(0.1*height), int(0.4*width)
			print(nh,nw)
			img = img[nh:-nh,:-nw]
		else:
			nh, nw = int(0.1*height), int(0.1*width)
			print(nh,nw)
			img = img[nh:-nh,nw:-2*nw]

		ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY) 
		ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU) 
		ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC) 
		ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO) 
		ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV) 

		gaussian = cv2.adaptiveThreshold(thresh1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)



		if target == 'shelf':
			kernel = np.ones((5,5), np.uint8)
			dilate = cv2.dilate(thresh3, kernel)
			final_text = getShelf(thresh3)
			#cv2.imshow('Truncated Threshold', thresh3)
			#cv2.imshow('Dilated', dilate)

			#cv2.imshow('Binary Threshold', thresh1) 
			#cv2.imshow('Binary Threshold Inverted', thresh2) 
			#cv2.imshow('Truncated Threshold', thresh3) 
			#cv2.imshow('Set to 0', thresh4) 
			#cv2.imshow('Set to 0 Inverted', thresh5)
			#cv2.imshow('Gaussian', th3)
			#cv2.imshow('Dilation', dilate)
			
			if cv2.waitKey(0) & 0xff == 27:  
				cv2.destroyAllWindows()  
		else: 	
			kernel = np.ones((3,3), np.uint8)
			dilate = cv2.dilate(thresh1, kernel)
			final_text = getLabel(gaussian)
			
			# cv2.imshow('Binary Thresholding', gaussian)
			# #cv2.imshow('Eroded', erode)
			# if cv2.waitKey(0) & 0xff == 27:  
			# 	cv2.destroyAllWindows() 
			

		  

		  
		# cv2.imshow('Binary Threshold', thresh1) 
		# cv2.imshow('Binary Threshold Inverted', thresh2) 
		# cv2.imshow('Truncated Threshold', thresh3) 
		# cv2.imshow('Set to 0', thresh4) 
		# cv2.imshow('Set to 0 Inverted', thresh5)
		# cv2.imshow('Gaussian', th3)
		#cv2.imshow('Dilation', dilate)

		 
		    
		 
		# if cv2.waitKey(0) & 0xff == 27:  
		# 	cv2.destroyAllWindows()  
		#print("EXtract", final_text)
		return final_text

if __name__ == "__main__":
	for file in os.listdir('roi/'):
		#image= Image.open('shelf/shelf' + str(i) + '.jpg')
		image = Image.open('roi/' + file)
		print(file)
	#image = cv2.imread("./test1.jpg")
		getText(image,'label')