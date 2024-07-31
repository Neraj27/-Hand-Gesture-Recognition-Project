<h1 align="center">Hand-Gesture-Recognition-Project</h1>

## 🛠 Libraries Used
- **cv2**: OpenCV library for computer vision tasks.
- **mediapipe**: MediaPipe library for hand tracking and gesture recognition.
- **pyautogui**: Library for controlling the mouse and keyboard to automate interactions with the computer.
- **time**: Standard Python library for time-related functions.

## 🎯 Features
- Real-time hand gesture recognition
- Simulates key presses based on the number of raised fingers
- Visualizes hand landmarks on the video feed

## 🚀 How It Works
1. **Hand Tracking**: Uses MediaPipe to detect hand landmarks in each video frame.
2. **Finger Counting**: Counts the number of raised fingers based on the positions of specific landmarks.
3. **Gesture Recognition**: Recognizes gestures based on the finger count and simulates corresponding key presses.
4. **Visualization**: Draws hand landmarks on the video frames for real-time visualization.
