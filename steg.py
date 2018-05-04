# steg.py
# author: Jack Skrable
# date: 05/03/2018
# desc: first attempt at lsb steganography decoding from image

from PIL import Image
import binascii

def main():
	
	# open image file
	im = Image.open('DZeGwV8UQAAUWnF.jpg')
	# load into matrix of pixels
	pix = im.load()
	# get width and height 
	#w, h = im.size()
	w = im.size[0]
	h = im.size[1]
	print("Width: ", w)
	print("Height: ", h)
	
	
	# init empty string for hidden bits
	msg = str()
	# iterate thru all pixels
	for i in range(w):
		for j in range(h):
			# get rgb vals for pixel
			rgb = pix[i,j]
			# iterate thru rgb bytes
			for k in rgb:
				# get binary representation of byte
				b = bin(k)
				# get lsb
				lsb = b[len(b)-1]
				# append lsb to msg
				msg += lsb
	
	#print(binascii.b2a_base64(msg))
	
	# open file for writing
	with open("bin.txt", "w") as outfile:
		outfile.write(msg)
		outfile.close()
		
	"""
	# debugging 
	rgb = pix[200,400]
	print("rgb: ",rgb)
	r = rgb[0]
	g = rgb[1]
	b = rgb[2]
	print("r: ", bin(r))
	print("lsb(r): ", bin(r)[len(bin(r))-1])
	print("g: ", bin(g))
	print("lsb(g): ", bin(g)[len(bin(g))-1])
	print("b: ", bin(b))
	print("lsb(b): ", bin(b)[len(bin(b))-1])
	"""
	
if __name__ == "__main__":
	main()