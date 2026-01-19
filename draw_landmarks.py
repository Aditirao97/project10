import cv2 
import mediapipe as mp

hand_mp = mp.solutions.hands.Hands()
drawing_utile =mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
while True :
    _,image = cap.read()
    rgb_color=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output=hand_mp.process(rgb_color)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utile.draw_landmarks(image,hand)
    cv2.imshow("hand",image)
    key=cv2.waitKey(5)
    if key==27:
        break
cv2.destroyAllWindows()
    

