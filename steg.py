# steg.py
# author: Jack Skrable
# date: 05/03/2018
# desc: first attempt at lsb steganography decoding from image

from PIL import Image

def main():
	
	# open image file
	im = Image.open('DZeGwV8UQAAUWnF.jpg')
	# load into matrix of pixels
	pix = im.load()
	# get width and height 
	w = im.size[0]
	h = im.size[1]
	print("Width: ", w)
	print("Height: ", h)
	
	"""
	# init empty string for hidden bits
	msg = None
	for i in w:
		for j in h:
			rgb = pix[i,j]
			r = rgb[0]
			g = rgb[1]
			b = rgb[2]
			
	"""		
		
	rgb = pix[200,400]
	r = rgb[0]
	g = rgb[1]
	b = rgb[2]
	print("r: ", bin(r))
	print("lsb(r): ", bin(r)[len(bin(r))-1])
	print("g: ", bin(g))
	print("lsb(g): ", bin(g)[len(bin(g))-1])
	print("b: ", bin(b))
	print("lsb(b): ", bin(b)[len(bin(b))-1])
if __name__ == "__main__":
	main()