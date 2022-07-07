#!/usr/bin/python3
import time

import time

import cv2

from picamera2 import Picamera2, Preview, MappedArray


eye_detector = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_eye.xml")


def draw_eyes(request):
    with MappedArray(request, "main") as m:
        for e in eyes:
            (x, y, w, h) = [c * n // d for c, n, d in zip(e, (w0, h0) * 2, (w1, h1) * 2)]
            cv2.rectangle(m.array, (x, y), (x + w, y + h), (0, 255, 0, 0))


picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
config = picam2.preview_configuration(main={"size": (640, 480)},
                                      lores={"size": (320, 240), "format": "YUV420"})
picam2.configure(config)

(w0, h0) = picam2.stream_configuration("main")["size"]
(w1, h1) = picam2.stream_configuration("lores")["size"]
s1 = picam2.stream_configuration("lores")["stride"]
eyes = []
picam2.post_callback = draw_eyes

picam2.start()

start_time = time.monotonic()
while time.monotonic() - start_time < 300:
    buffer = picam2.capture_buffer("lores")
    grey = buffer[:s1 * h1].reshape((h1, s1))
    eyes = eye_detector.detectMultiScale(grey, 1.12, 15)
