from sense_hat import SenseHat
sense=SenseHat()
X=[0,0,255]
O=[255,255,255]
custom_mark=[
	O,O,O,X,X,O,O,O,
	O,O,X,O,O,X,O,O,
	O,O,O,O,O,X,O,O,
	O,O,O,O,X,O,O,O,
	O,O,O,X,O,O,O,O,
	O,O,O,X,O,O,O,O,
	O,O,O,O,O,O,O,O,
	O,O,O,X,O,O,O,O,
]
sense.set_pixels(custom_mark)
