# Implement-Adaptive-Thresholding-Using-the-Integral-Image
---
This is an implementation of the method suggested in a paper entitled Adaptive [Thresholding using the Integral Image](https://www.researchgate.net/publication/220494200_Adaptive_Thresholding_using_the_Integral_Image) in my master's program.

This is my implementation of an adaptive focusing technique applied in real-time image processing (streaming).

The main purpose of image thresholding in mistaken image processing helps to classify pixels in two areas of _light (light)_ and _dark (dark)_ in an image. Adaptive thresholding is a form of thresholding that takes into account how the illumination is located in space in an image.

The real-time adaptive thresholding method is implemented using the input integral image. This is a simple, powerful and easy to implement method. This technique is suitable for processing live video streams at standard real-time frame rates. In addition, the above method is also applied in advanced image processing or computer graphics applications.

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
