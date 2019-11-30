import request
import sys
from draw import draw_image
from PIL import Image

class Face:
	""" Class Face. Contains a rectangle and a gender """

	def __init__(self, gender, width, height):
		self.width = width
		self.height = height
		self.gender = gender

def __is_image(path):
	""" Check if given path is a image """

	try:
		test = Image.open(path)
		test.close()
	except IOError:
		return False
	return True

def run():
	""" Run script """

	if len(sys.argv) is not 2 or not __is_image(sys.argv[1]):
		print("Usage: python3 srcs/main.c <Image PATH>")
		sys.exit(0)

	print("Loading file..")
	try:
		with open(sys.argv[1], 'rb') as image_raw:
			faces = request.request_faces(image_raw)
			if len(faces) == 0:
				print("No face found!")
				sys.exit(0)
			draw_image(sys.argv[1], faces)

	except IOError as error:
		print("(%s)" % error)

if __name__ == '__main__':
	run()
