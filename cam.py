import cv2
def take_photo():
	camera_port = 0

	ramp_frames = 30

	camera = cv2.VideoCapture(camera_port)

	def get_image():
		retval, im = camera.read()
		return im

	for i in range(ramp_frames):
		temp = get_image()

	print("Capturing face")

	camera_capture = get_image()
	file = "test.png"
	cv2.imwrite(file, camera_capture)

	del camera
take_photo()