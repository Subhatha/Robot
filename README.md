Project Documentation
Robotics

Human Following Robot using raspberry pi + Arduino

By – Subhatha Kaumud Senanayake



Version 1.0




































Description of the project 

This project is about making a Human recognition Robot using raspberry and Arduino while being able to avoid obstacles, the robot will use machine learning and computer vision to detect a certain human to follow, and ultrasonic sensors will help to avoid anything comes in.

Purpose of the project 

To create a robot which can follow any object or a person using a USB camera
To train a custom image model using personal images
To avoid obstacles comes to it 
To understand AI and Machine Learning fundamentals


Libraries and Frameworks 

Computer Vision  
Open CV (Python) – Handles the images using live video

Machine Learning 
TensorFlow – Image model training (200) images 

Data Processing 
NumPY and Matplotlib – Image array handling and Accuracy 

Data Labeling 
LabelImg – to label images (free)
https://github.com/HumanSignal/labelImg/releases

Documentation 
MS 365 for Documenting 
Github – Document hosting and Code hosting 
https://github.com/Subhatha/Robot
Draw.io – Algorithms and structure making
 


Architecture 

Hardware Components 

•	Raspberry pi 400 (Given version from the lab)
•	Arduino Uno
•	USB Camera
•	Ultrasonic sensor
•	Motor driver 
•	Dc Motors and wheels
•	Chassy
•	Battery pack





Software Architecture and the Flow 







































Image Model 

Resized to 224*224 normalized value pixels 

•	200 images 
•	Front  - 50
•	Back – 50
•	Left side – 50
•	Right side – 50

20 Validation images (random captured)

Dataset split to 2 parts – 80% for training and 20% for validation for better accuracy.


Human following Decisions 

I made 5 Decisions for the model 

•	Person_Front – Move Forward
•	Person_Left – Turn Left
•	Person_Right – Turn Right
•	Person_Back – Stop (not implemented yet)
•	No_Person – Idle/Stop/Search (can make a rotation 360 degrees until it detect a person


Future Improvements

•	Add a Depth camera for more accuracy
•	360 Degrees of FOV
•	Increase the Dataset size






References


https://www.tensorflow.org/tutorials
https://pypi.org/project/opencv-python/

<img width="451" height="684" alt="image" src="https://github.com/user-attachments/assets/7d7aa1ca-1575-4860-83c8-07597cd41f1a" />
