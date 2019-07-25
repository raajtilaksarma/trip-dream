import cv2
from dream import getDreamImage

video_capture = cv2.VideoCapture(0)

def camera_stream():
    while True:
        # Capture frame-by-frame        
        ret, frame = video_capture.read()
        cv2.imwrite("images/frame.jpg",frame) 
        out_frame = getDreamImage('images/frame.jpg')
        ret, jpeg = cv2.imencode('.jpg', out_frame)
        return jpeg.tobytes()
