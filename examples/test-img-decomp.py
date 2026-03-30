import cv2
import os

VIDEO_PATH = '/Users/jacob/Documents/teaching/corpus-jade/Reportage n°56.mp4'
INTERVAL = 5
OUTPUT_DIR = os.path.join(os.getcwd(), "IMGS-OUT")

if os.path.isdir(OUTPUT_DIR) == False:
    os.makedirs(OUTPUT_DIR)

cap = cv2.VideoCapture(VIDEO_PATH)
fps = cap.get(cv2.CAP_PROP_FPS)

print(fps)

frame_count = 0
frame_interval = int(fps * INTERVAL)
save_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        file_name = os.path.join(OUTPUT_DIR, f"image_{save_count}.jpg")
        cv2.imwrite(file_name, frame)
        save_count = save_count + 1

    frame_count = frame_count + 1    

print(frame_count)