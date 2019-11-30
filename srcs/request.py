import requests
import base64
import sys
import os
from config import *
from main import Face

API_URL = "https://api-us.faceplusplus.com/facepp/v3/detect"

def __parse_face(json_element):
	""" Given a JSON String, extract informations and parse into Face object """

	if json_element is None or "attributes" not in json_element:
		return None
	gender = json_element["attributes"]["gender"]["value"]
	rec = json_element["face_rectangle"]
	width = (rec["left"], rec["left"] + rec["width"])
	height = (rec["top"], rec["top"] + rec["height"])
	return Face(gender, width, height)

def request_faces(image_raw):
	""" Request Face++ API and return a list of Face """

	if API_KEY is "YOUR_KEY":
		print("You need to add your API access into srcs/config.py first!")
		sys.exit(0)
	image_base64 = base64.b64encode(image_raw.read())
	payload = {
		'api_key': API_KEY,
		'api_secret': API_SECRET,
		'image_base64': image_base64,
		'return_attributes': 'gender'
	}

	response = requests.post(API_URL, data=payload)
	json_data = response.json()
	faces = []
	for json_element in json_data["faces"]:
		parsed_face = __parse_face(json_element)
		if parsed_face is not None:
			faces.append(parsed_face)
	return faces
