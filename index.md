# Detecting Unattentive Car Drivers
 
This project uses a Raspberry Pi machine learning program to detect whether the driver of a car is attentive or not. If the driver is looking down or has their eyes closed, the speaker will try to alert the driver.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Shuvam | Moreau Catholic High School | Computer Science | Incoming Junior

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLXQZU8QvJV9rAtq2BbXbuaYxf8qZCV4ncQU251ZyZJFHK20Bq_x2f0YFLaRgdEAiVJ9I6s7ESH9mFThj_BKtDviE-diiHyiSX73TIQUTpSs4AENXl9nicOyVBilNvOptstkM9RLaF_ECU4J06S_LEF7=w726-h725-no?authuser=0)


# Third Milestone

My third milestone was to get the Raspberry Pi to successfully recognize whether a person's eyes were open. Separate programs based on the same code recognized a human face and whether a person was smiling. In the code, the time , OpenCV, and Raspberry Pi camera libraries were imported. Then, the CascadeClassifier() is used to import the haarcascade_eye.xml file, trained with positive and negative images. Then the draw_eyes() function draws a rectangle around the detected eyes. Next, the camera is configured, and the preview window shows what the camera is streaming. Then the program is run for 300 seconds using a while loop. The detectMultiScale() function is used to recognize the eyes. It takes in 3 arguments: the images captured by the camera, the scale factor and the minimum neighbors. The scale factor is how much the image captured by the camera should be adjusted by, so that the program can detect the eyes whether they are close or far to the camera. The min neighbors argument allows you to accuraetly detect the eyes by only drawing rectangles around the areas where the program is more confident there are eyes. Depending on the scale factor and min neighbors arguments inputted by the programmer (which takes trial and error to get right), the program's efficiency can change.  

# Second Milestone

My second milestone was to get the Raspberry Pi to successfully complete basic image recognition. When the camera was pointed towards an object, it would go through a file of objects it was trained to recognize, and determine whether the camera was capturing a recognizable object. In the code, the tensorflow, Numpy, and OpenCV2 libraries were installed to help with the machine learning process. The sys library was imported, which would help run the program. The os library would help the program access files and directories already stored in the Raspberry Pi's finder. The argparse library enabled the command line in the terminal to be used to run the code. Then from the PIL (Python Imaging Library) library, the Image, ImageFont, and ImageDraw functions were imported. Lastly, the Picamera2 library is important to code the camera. Then first function, ReadLabelFile(), reads the file provided, which contains the list of objects that the program can recognize. The next function, DrawRectangles(), draws a rectanggles around the recognized object. The InferenceTensorFlow() function uses tensorflow and OpenCV to compate the image to the training data, and if the image is greater than 50% similar to the training data, it will be labeled and a rectangle will be drawn around it. Then lastly, the main() function starts the running of the code.

[![Shuvam Sinha Milestone 2](https://res.cloudinary.com/marcomontalbano/image/upload/v1656517374/video_to_markdown/images/youtube--MF82jj59V1g-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=MF82jj59V1g "Shuvam Sinha Milestone 2")

# First Milestone
  
My first milestone was setting up the Raspberry Pi and installing the camera (Picamera2). A preview of what the camera was capturing was shown, and once a widget was clicked, the camera would take a picture and save it to the desktop. In the code, the PyQT5 library was installed in order to enhance the user interface and add widgets. Then the Picamera2 library was imported, allowing me to code the camera. The post_callback() function uses a request.get.metadata().items() function in order to display the metadata of the image next to the preview. The camera is then configured to preview an image of 800 by 600 pixels. Then, when the widget saying "Click to capture JPEG" is clicked, the on_button_clicked() function is triggered. If there is not a previous image already in the process of being synced, the image is captured. Then the contents of the preview window are coded, and the prgram is told to start functioning.

[![Shuvam Sinha Milestone 1](https://res.cloudinary.com/marcomontalbano/image/upload/v1655912377/video_to_markdown/images/youtube--sTCEz6GNhDo-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=sTCEz6GNhDo "Shuvam Sinha Milestone 1")

# Starter Project: Custom Arduino Project

First, I learned how the ultrasonic distance sensor and servo worked. The ultrasonic sensor first sends out a signal that humans can not feel or hear. If an object is in range, the signal bounces off of the object and is read by the sensor again.  The Servo arm has a rotation of 180 degrees, and it is able to move to the desired degree. I then installed the Arduino, and mapped out the circuit I was trying to build. After connecting the sensors and motors to the Arduino, I programmed the circuit. I made the ultrasonic sensor detect the distance of the object in front of it by multiplying the duration (time it takes for the sensor between sending and recieving the signal) by 0.0343 (the speed of sound - 343 meters per second - is converted to 0.0343 centimeters per microsecond because the sensor is calculating in centimeters and microseconds) and then dividing that by 2. Then, if the distance is between 2 and 60 cm, the servo would move to the according degrees.

Here is the mapping of the Arduino I created using TinkerCad:
![Arduino Model - TinkerCad](https://user-images.githubusercontent.com/97251821/174340128-64b7c9a0-240e-44ee-bf98-838628f14f96.png)

Here is the video of the project:

[![Shuvam Sinha Starter Project](https://res.cloudinary.com/marcomontalbano/image/upload/v1655740323/video_to_markdown/images/youtube--fmgGCqnGbXc-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=fmgGCqnGbXc "Shuvam Sinha Starter Project")
