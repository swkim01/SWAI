import picamera2, time

#camera = picamera2.Picamera2()
#
#try:
#  camera.start_preview(picamera2.Preview.QTGL)
#  camera.start()
#  time.sleep(10)
#  camera.stop_preview()
#finally:
#  camera.close()

with picamera2.Picamera2() as camera:
   camera.resolution = (640, 480)
   camera.start_preview(picamera2.Preview.QTGL)
   camera.start()
   time.sleep(10)
   camera.stop_preview()
