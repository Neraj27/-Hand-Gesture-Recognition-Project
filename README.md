# -Hand-Gesture-Recognition-Project
This project uses computer vision and machine learning techniques to recognize hand gestures in real-time. The script captures video frames from a webcam, detects hand landmarks using MediaPipe, and simulates key presses based on the recognized gestures.

Libraries Used
cv2: OpenCV library for computer vision tasks.
mediapipe: MediaPipe library for hand tracking and gesture recognition.
pyautogui: Library for controlling the mouse and keyboard to automate interactions with the computer.
time: Standard Python library for time-related functions.
Features
Real-time hand gesture recognition.
Simulates key presses based on the number of raised fingers.
Visualizes hand landmarks on the video feed.
How It Works
Hand Tracking: Uses MediaPipe to detect hand landmarks in each video frame.
Finger Counting: Counts the number of raised fingers based on the positions of specific landmarks.
Gesture Recognition: Recognizes gestures based on the finger count and simulates corresponding key presses.
Visualization: Draws hand landmarks on the video frames for real-time visualization.
