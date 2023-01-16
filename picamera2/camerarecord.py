import picamera2, time

with picamera2.Picamera2() as camera:
   camera.resolution = (640, 480)
   video_config = camera.create_video_configuration()
   camera.configure(video_config)
   encoder = picamera2.encoders.H264Encoder(10000000)
   camera.start_recording(encoder, 'foo.h264')
   #camera.wait_recording(60)
   time.sleep(10)
   camera.stop_recording()
