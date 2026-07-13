# AwakeAI - AI-Based Driver Drowsiness Detection System

## Project Overview

AwakeAI is an Artificial Intelligence-based driver drowsiness detection system designed to improve road safety by monitoring driver alertness through computer vision techniques.

The system analyzes facial features, particularly eye movements, using real-time face landmark detection. By calculating the Eye Aspect Ratio (EAR), it identifies prolonged eye closure patterns and triggers an alert when signs of drowsiness are detected.

This project provides a non-invasive and cost-effective solution for fatigue monitoring in transportation and safety-critical environments.

---

## Problem Statement

Driver fatigue is a major contributor to road accidents worldwide. Traditional monitoring methods depend on manual observation and are not effective for continuous alertness assessment.

A smart vision-based system is required to automatically detect signs of driver fatigue and provide immediate warnings to prevent accidents.

---

## Proposed Solution

AwakeAI uses computer vision and machine learning techniques to continuously analyze facial landmarks from a video stream.

The system:

* Detects the driver's face
* Extracts eye landmarks using MediaPipe Face Mesh
* Calculates Eye Aspect Ratio (EAR)
* Determines whether the eyes remain closed for a prolonged duration
* Generates an audio alert when drowsiness is detected

---

## Key Features

* Real-time face and eye landmark detection
* Eye Aspect Ratio-based drowsiness classification
* Automatic alarm generation
* Video-based monitoring support
* Lightweight computer vision implementation
* Expandable for real-time webcam and vehicle integration

---

## Technology Stack

### Programming Language

* Python

### Computer Vision Frameworks

* OpenCV
* MediaPipe Face Mesh

### Python Libraries

* NumPy
* Pygame

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## System Architecture

```
                    Video Input
                         |
                         |
                         v
              Face Detection Module
                         |
                         |
                         v
          Facial Landmark Extraction
                         |
                         |
                         v
             Eye Aspect Ratio (EAR)
                         |
                         |
                         v
              Drowsiness Analysis
                         |
              ---------------------
              |                   |
              v                   v
           Alert State        Normal State
              |
              |
              v
          Audio Warning
```

---

## Working Methodology

### 1. Face Detection

The system uses MediaPipe Face Mesh to identify facial landmarks from the input video stream.

### 2. Eye Landmark Extraction

Specific landmark points around both eyes are extracted to analyze eye movements and closure patterns.

### 3. Eye Aspect Ratio Calculation

The Eye Aspect Ratio is calculated using vertical and horizontal distances between eye landmarks.

```
EAR = (Vertical Eye Distances) / (Horizontal Eye Distance)
```

A lower EAR value indicates reduced eye opening.

### 4. Drowsiness Detection

When the EAR value remains below a predefined threshold for multiple consecutive frames, the system identifies a drowsiness condition and activates the warning mechanism.

---

## Project Structure

```
AwakeAI/
│
├── drowsiness_detector.py
├── main.py
├── alarm.wav
├── requirements.txt
├── README.md
└── input.mp4
```

---

## Installation and Setup

### Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/AwakeAI-Drowsiness-Detection.git
```

### Navigate to Project Directory

```
cd AwakeAI-Drowsiness-Detection
```

### Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Execute the following command:

```
python drowsiness_detector.py
```

The application will start video processing and display the Eye Aspect Ratio value. If prolonged eye closure is detected, an alert message and alarm sound will be generated.

---

## Requirements

```
opencv-python
mediapipe==0.10.14
numpy
pygame
```

---

## Future Enhancements

* Real-time webcam-based driver monitoring
* Voice-based warning system
* Drowsiness severity scoring
* Driver fatigue analytics dashboard
* Mobile and IoT integration
* Cloud-based monitoring system
* Integration with vehicle safety systems

---

## Applications

* Automotive safety systems
* Fleet management solutions
* Transportation monitoring
* Smart vehicle technologies
* Driver assistance systems

---

## Contributors

AwakeAI Development Team

---

## License

This project is developed for educational and research purposes.
