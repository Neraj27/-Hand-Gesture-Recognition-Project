import cv2 #cv2: OpenCV library for computer vision tasks.
import mediapipe  as mp #mediapipe: The MediaPipe library for hand tracking and gesture recognition.
import pyautogui # Library for controlling the mouse and keyboard to automate interactions with the computer.
import time # Standard Python library for time-related functions.

# define a function to count the number of fingers raised.
def count_fingers(lst): 
    cnt = 0
    thresh = (lst.landmark[0].y*100-lst.landmark[9].y*100)/2
    
    if (lst.landmark[5].y*100-lst.landmark[8].y*100) > thresh:
        cnt+=1
        
    if (lst.landmark[5].y*100-lst.landmark[12].y*100) > thresh:
        cnt+=1
        
    if (lst.landmark[13].y*100-lst.landmark[16].y*100) > thresh:
        cnt+=1
        
    if (lst.landmark[17].y*100-lst.landmark[20].y*100) > thresh:
        cnt+=1
        
    if (lst.landmark[5].x*100-lst.landmark[4].x*100) > 5 :
        cnt+=1  
    
    return cnt
    
# initalizes the object named cap using OpenCV-> class VideoCapture to capture video frames from camera.
cap = cv2.VideoCapture(0)

drawing =mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)
prev = -1

start_init=False

# starts infinate loop to capture video frames
while True:
    end_time=time.time()
    _, frm=cap.read()
    frm=cv2.flip(frm,1)
    res= hand_obj.process(cv2.cvtColor(frm,cv2.COLOR_BGR2RGB))
    
    #if the hand is detected then it calculates the no of fingers raised using count_fingers function 
    if res.multi_hand_landmarks:
        hand_keypoints = res.multi_hand_landmarks[0]
        cnt= count_fingers(hand_keypoints)
        
        #checks if current detected finger count is same as the previous finger count 
        if not(prev==cnt):
            if not (start_init):
                start_init = time.time()
                start_init = True
                
             # after the time laps of 1 second the specified key is pressed on the keyboard using pyaotugui based on the no og finger count     
            elif (end_time-start_init) > 1:
        
                if (cnt==1):
                    pyautogui.press("right")
                    
                elif (cnt==2):
                    pyautogui.press("left")
                    
                elif (cnt==3):
                    pyautogui.press("up")
                    
                elif (cnt==4):
                    pyautogui.press("down")
                    
                elif (cnt==5):
                    pyautogui.press("space")
                
                prev=cnt
                start_init=False
                
        #  This line draws the detected hand landmarks on the video frame for visualization purposes.          
        drawing.draw_landmarks(frm,hand_keypoints,hands.HAND_CONNECTIONS)

    # used to exit the loop by pressing the escape key(27)
    cv2.imshow("Media Player control Using Hand gestures",frm)

    if cv2.waitKey(1)==27:
        cv2.destroyAllWindows()
        cap.release()
        break