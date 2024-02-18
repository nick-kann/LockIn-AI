import cv2
import mediapipe as mp
import pyautogui
import numpy as  np
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Screen size for mouse control
screen_width, screen_height = pyautogui.size()
pyautogui.FAILSAFE = False

keep_running = True

# Convert hand landmarks to pixel coordinates
def landmark_to_pixel(hand_landmarks, frame_width, frame_height):
    coords = {}
    for id, lm in enumerate(hand_landmarks.landmark):
        coords[id] = (int(lm.x * frame_width), int(lm.y * frame_height))
    return coords

def distance(point_one, point_two):
    return math.sqrt((point_one[0] - point_two[0])**2 + (point_one[1] - point_two[1])**2)

# Process hand actions
def process_hand_actions(coords, frame_width, frame_height):
    index_tip = coords[8]
    x_scaled = np.interp(index_tip[0], (0, frame_width), (0, screen_width))
    y_scaled = np.interp(index_tip[1], (0, frame_height), (0, screen_height))
    pyautogui.moveTo(x_scaled, y_scaled)


    thumb_tip = coords[4]
    middle_tip = coords[12]
    ring_tip= coords[16]
    pinky_tip= coords[20]

    if distance(coords[6], thumb_tip )< 25:  # Threshold for clicking
        pyautogui.click()
    if distance(middle_tip, thumb_tip )< 50:  # Threshold for clicking
        pyautogui.click(button='right')
    if distance(index_tip,middle_tip)<40:
        if(index_tip[1]<coords[0][1]):
            pyautogui.scroll(1)
        else:
            pyautogui.scroll(-1)

def main():
    cap = cv2.VideoCapture(0)
    while keep_running:
        success, frame = cap.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hands.process(rgb_frame)
        hand_landmarks = output.multi_hand_landmarks

        if hand_landmarks:
            for handLms in hand_landmarks:
                mp_drawing.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                coords = landmark_to_pixel(handLms, frame_width, frame_height)
                process_hand_actions(coords, frame_width, frame_height)

        #cv2.imshow('Virtual Mouse', frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

