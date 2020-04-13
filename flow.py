from darknet_multiple import *
from matching import *

for filename in os.listdir("test_images"):
    filename = "test_images/" + filename 
    print(filename)
    result = performDetect(imagePath=filename)
    extractLabels(result)
