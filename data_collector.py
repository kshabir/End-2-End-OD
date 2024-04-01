import os
from tkinter import image_types
import cv2
import time
import uuid

print("Hello world")

IMAGE_PATH = "CollectedImages"

labels = ['Hello', 'Yes', 'N0', 'Thanks', 'IloveYou', 'Please']

number_of_images = 10

for label in labels:
    image_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(image_path)

    # Open Cam
    cap = cv2.VideoCapture(0)

    # Set the desired resolution (width, height)
    desired_width = 640
    desired_height = 480

    # Set the resolution of the camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

    print(f"Collecting Images for {label}")
    time.sleep(3)

    for imag_num in range(number_of_images):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        imageName = os.path.join(IMAGE_PATH, label, label+ '.'+' {}.jpg'.format(str(uuid.uuid1())))

        cv2.imwrite(imageName, frame)

        cv2.imshow(label,frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    #cv2.destroyAllWindows()

