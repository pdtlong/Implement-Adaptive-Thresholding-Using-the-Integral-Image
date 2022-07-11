# Implement-Adaptive-Thresholding-Using-the-Integral-Image
---
This is an implementation of the method suggested in a paper entitled Adaptive [Thresholding using the Integral Image](https://www.researchgate.net/publication/220494200_Adaptive_Thresholding_using_the_Integral_Image) in my master's program.

- This is a method of solving the problem of the change in brightness in a photo. This method uses adaptive thresholding.
- The key to this method is that each pixel in the image is assigned a different threshold value. There are many methods for getting the upper threshold, but within the scope of the article above, we will mention using integral image.

<center><img src="https://user-images.githubusercontent.com/55480300/178339227-88769cf9-90f8-4eca-85ef-9aaa3d78a841.png" width="650"/></center>

- **Pros**: Capable of handling images in online conditions if the device is powerful enough.
- **Cons**: Due to the focus on speed and light balance, some details can be overlooked
---
## Required libraries:
- Python 3.7
- imutils
- numpy 
- cv2
- os
## How to run??

Python Realtime_thresholding.py 
