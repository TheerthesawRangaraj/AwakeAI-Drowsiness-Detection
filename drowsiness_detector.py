import cv2
import mediapipe as mp
import numpy as np
import pygame
import time


# Initialize alarm sound
pygame.mixer.init()


def alarm():
    pygame.mixer.music.load("alarm.wav")
    pygame.mixer.music.play()


# MediaPipe face mesh
mp_face = mp.solutions.face_mesh

face_mesh = mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)


# Eye landmark points
LEFT_EYE = [362,385,387,263,373,380]
RIGHT_EYE = [33,160,158,133,153,144]


def calculate_EAR(eye):

    A = np.linalg.norm(
        np.array(eye[1])-np.array(eye[5])
    )

    B = np.linalg.norm(
        np.array(eye[2])-np.array(eye[4])
    )

    C = np.linalg.norm(
        np.array(eye[0])-np.array(eye[3])
    )

    ear = (A+B)/(2*C)

    return ear



# Open video
cap = cv2.VideoCapture("input.mp4")



EAR_THRESHOLD = 0.22

COUNTER = 0

ALARM_ON = False


while True:

    ret, frame = cap.read()

    if not ret:
        break


    frame = cv2.resize(frame,(900,600))

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    result = face_mesh.process(rgb)


    if result.multi_face_landmarks:


        for face_landmarks in result.multi_face_landmarks:


            h,w,_ = frame.shape


            left=[]
            right=[]


            for id in LEFT_EYE:

                x=int(
                    face_landmarks.landmark[id].x*w
                )

                y=int(
                    face_landmarks.landmark[id].y*h
                )

                left.append([x,y])


            for id in RIGHT_EYE:

                x=int(
                    face_landmarks.landmark[id].x*w
                )

                y=int(
                    face_landmarks.landmark[id].y*h
                )

                right.append([x,y])



            left_EAR=calculate_EAR(left)
            right_EAR=calculate_EAR(right)


            EAR=(left_EAR+right_EAR)/2



            cv2.putText(
                frame,
                f"EAR: {round(EAR,2)}",
                (30,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )


            if EAR < EAR_THRESHOLD:

                COUNTER +=1


                if COUNTER > 20:


                    cv2.putText(
                        frame,
                        "DROWSINESS ALERT!",
                        (150,300),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0,0,255),
                        4
                    )


                    if not ALARM_ON:

                        alarm()
                        ALARM_ON=True


            else:

                COUNTER=0
                ALARM_ON=False



    cv2.imshow(
        "AI Driver Drowsiness Detection",
        frame
    )


    if cv2.waitKey(1)==27:
        break



cap.release()
cv2.destroyAllWindows()