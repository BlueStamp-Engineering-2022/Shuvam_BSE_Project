# BlueStamp Project
This project uses an Arduino, ultrasonic distance sensor, and a servo arm and motor. Depending on how far an object is to the ultrasonic distance sensor, the servo arm will move to a specific position. As the object goes farther, the arm moves counter-clockwise, and as the object moves closer, the arm moves clockwise.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Shuvam Sinha | Moreau Catholic High School | Computer Science | Incoming Junior

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLXQZU8QvJV9rAtq2BbXbuaYxf8qZCV4ncQU251ZyZJFHK20Bq_x2f0YFLaRgdEAiVJ9I6s7ESH9mFThj_BKtDviE-diiHyiSX73TIQUTpSs4AENXl9nicOyVBilNvOptstkM9RLaF_ECU4J06S_LEF7=w726-h725-no?authuser=0)


# Final Milestone
My final milestone is the increased reliability and accuracy of my robot. I ameliorated the sagging and fixed the reliability of the finger. As discussed in my second milestone, the arm sags because of weight. I put in a block of wood at the base to hold up the upper arm; this has reverberating positive effects throughout the arm. I also realized that the forearm was getting disconnected from the elbow servo’s horn because of the weight stress on the joint. Now, I make sure to constantly tighten the screws at that joint. 

[![Final Milestone](https://res.cloudinary.com/marcomontalbano/image/upload/v1612573869/video_to_markdown/images/youtube--F7M7imOVGug-c05b58ac6eb4c4700831b2b3070cd403.jpg )](https://www.youtube.com/watch?v=F7M7imOVGug&feature=emb_logo "Final Milestone"){:target="_blank" rel="noopener"}

# Second Milestone
My final milestone is the increased reliability and accuracy of my robot. I ameliorated the sagging and fixed the reliability of the finger. As discussed in my second milestone, the arm sags because of weight. I put in a block of wood at the base to hold up the upper arm; this has reverberating positive effects throughout the arm. I also realized that the forearm was getting disconnected from the elbow servo’s horn because of the weight stress on the joint. Now, I make sure to constantly tighten the screws at that joint.

[![Third Milestone](https://res.cloudinary.com/marcomontalbano/image/upload/v1612574014/video_to_markdown/images/youtube--y3VAmNlER5Y-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=y3VAmNlER5Y&feature=emb_logo "Second Milestone"){:target="_blank" rel="noopener"}
# First Milestone
  

My first milestone was setting up and hooking up the Raspberry Pi and all the necessary components onto my tv. The heatsinks, the sd card, and the controller were all added to ensure that the Raspberry Pi was working. Instead of the Raspberry Pi Os software, I had to first download a different software called Retro Pie. With Retro Pie, I needed to download an Imager for Raspberry Pi. Raspberry Pi Imager automatically downloads a list of the latest versions of Raspbian supported by the Raspberry Pi. Raspbian is the typical Raspberry Pi Os software, the one I needed on the Raspberry Pi was Retro Pi. With the included SD card, I plugged in the SD into my computer and launched the Imager. The imager allowed me to set the Operating System to Retro Pi instead of Raspbian onto the SD card. With the OS imaged onto the SD, I plugged the SD card back into the Raspberry Pi and rebooted the system and Retro Bi booted up.

[![First Milestone](https://res.cloudinary.com/marcomontalbano/image/upload/v1612574117/video_to_markdown/images/youtube--CaCazFBhYKs-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=CaCazFBhYKs "First Milestone"){:target="_blank" rel="noopener"}
# Starter Project: Custom Arduino Project

First, I learned how the ultrasonic distance sensor and servo worked. The ultrasonic sensor first sends out a signal that humans can not feel or hear. If an object is in range, the signal bounces off of the object and is read by the sensor again.  The Servo arm has a rotation of 180 degrees, and it is able to move to the desired degree. I then installed the Arduino, and mapped out the circuit I was trying to build. After connecting the sensors and motors to the Arduino, I programmed the circuit. I made the ultrasonic sensor detect the distance of the object in front of it by multiplying the duration (time it takes for the sensor between sending and recieving the signal) by 0.0343 (the speed of sound - 343 meters per second - is converted to 0.0343 centimeters per microsecond because the sensor is calculating in centimeters and microseconds) and then dividing that by 2. Then, if the distance is between 2 and 60 cm, the servo would move to the according degrees.

Here is the mapping of the Arduino I created using TinkerCad:
![Start Simulating](https://user-images.githubusercontent.com/97251821/174340128-64b7c9a0-240e-44ee-bf98-838628f14f96.png)

Here is the video of the project:

[![Shuvam Sinha Starter Project](https://res.cloudinary.com/marcomontalbano/image/upload/v1655740323/video_to_markdown/images/youtube--fmgGCqnGbXc-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=fmgGCqnGbXc "Shuvam Sinha Starter Project")
