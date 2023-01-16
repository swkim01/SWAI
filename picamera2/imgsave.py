import time
import picamera2

with picamera2.Picamera2() as camera:
   camera.resolution = (1280, 720)
   camera.start_preview(picamera2.Preview.QTGL)
   camera.exposure_compensation = 2
   camera.exposure_mode = 'spotlight'
   camera.meter_mode = 'matrix'
   camera.image_effect = 'gpen'
   camera.start()
   # Give the camera some time to adjust to conditions
   time.sleep(2)
   #camera.exif_tags['IFD0.Artist'] = 'Kim'
   #camera.exif_tags['IFD0.Copyright'] = 'Copyright (c) 2014 Kim'
   camera.capture_file('foo.jpg')
   camera.stop_preview()
