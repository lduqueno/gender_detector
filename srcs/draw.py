from PIL import Image, ImageDraw

def draw_image(path, faces):
	""" Draw found rectangles and genders on image """

	base = Image.open(path).convert('RGBA')
	copy = Image.new('RGBA', base.size, (255, 255, 255,0))
	draw = ImageDraw.Draw(copy)

	for elem in faces:
		start_bound = (elem.width[0], elem.height[0])
		end_bound = (elem.width[1], elem.height[1])
		draw.rectangle([start_bound, end_bound], outline="red")
		draw.text((start_bound[0] + (end_bound[0] - start_bound[0]) / 2 - 12,
			start_bound[1] - 15), elem.gender, fill="red")

	out = Image.alpha_composite(base, copy)
	out.show()
