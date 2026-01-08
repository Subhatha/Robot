🤖 Human Following Robot

Using Raspberry Pi + Arduino

Author: Subhatha Kaumud Senanayake
Version: 1.0

📌 Project Overview

This project implements a Human Following Robot using Raspberry Pi and Arduino, integrating Computer Vision and Machine Learning to recognize and follow a specific person while avoiding obstacles.

A USB camera is used for real-time human detection, and ultrasonic sensors help the robot detect and avoid obstacles in its path. The system is designed to understand the fundamentals of AI, Machine Learning, and Robotics integration.

🎯 Project Objectives

Build a robot capable of following a human using a USB camera

Train a custom image classification model using personal images

Implement obstacle avoidance using ultrasonic sensors

Learn and apply AI & Machine Learning fundamentals

Integrate Raspberry Pi and Arduino for real-time robotic control

🧠 Technologies & Libraries
🔍 Computer Vision

OpenCV (Python) – Real-time image processing from live video feed

🤖 Machine Learning

TensorFlow – Custom image classification model training

📊 Data Processing

NumPy – Image array manipulation

Matplotlib – Accuracy and result visualization

🏷 Data Labeling

LabelImg – Image annotation tool
👉 https://github.com/HumanSignal/labelImg/releases

📄 Documentation & Tools

MS 365 – Project documentation

GitHub – Code & documentation hosting
👉 https://github.com/Subhatha/Robot

Draw.io – System architecture & flow diagrams

🏗 System Architecture
🔧 Hardware Components

Raspberry Pi 400

Arduino Uno

USB Camera

Ultrasonic Sensor

Motor Driver

DC Motors & Wheels

Robot Chassis

Battery Pack

⚙️ Software Architecture & Flow

USB camera captures live video feed

OpenCV processes frames in real time

TensorFlow model classifies human position

Decision logic determines robot movement

Arduino controls motors based on commands

Ultrasonic sensors detect obstacles and stop/avoid

🖼 Image Classification Model

Input Size: 224 × 224 pixels

Normalization: Applied

Total Images: 200

Dataset Distribution:

Front: 50 images

Back: 50 images

Left: 50 images

Right: 50 images

Validation:

20 randomly captured images

80% Training / 20% Validation split for better accuracy

🚦 Human-Following Decisions

The model makes 5 classification decisions:

Classification	Robot Action
Person_Front	Move Forward
Person_Left	Turn Left
Person_Right	Turn Right
Person_Back	Stop (not implemented yet)
No_Person	Idle / Stop / Search (360° rotation)
🚀 Future Improvements

Integrate a Depth Camera for improved accuracy

Enable 360° Field of View (FOV)

Increase dataset size for better model performance

Implement Person_Back behavior

Improve obstacle avoidance logic

📚 References

TensorFlow Tutorials
👉 https://www.tensorflow.org/tutorials

OpenCV Python
👉 https://pypi.org/project/opencv-python/

📜 License

This project is developed for educational and experimental purposes.
