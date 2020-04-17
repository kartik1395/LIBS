from darknet_multiple import *
from matching import *
from docx.shared import Inches
from datetime import datetime


document= Document()
document.add_heading('Misplaced Books Report')

for filename in os.listdir("test_images"):
    filename = "test_images/" + filename 
    print(filename)
    result = performDetect(imagePath=filename)
    extractLabels(result, document)

document.save('Misplaced.docx')
print("Document Saved")