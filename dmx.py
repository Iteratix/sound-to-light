import pyenttec as dmx
from random import randint

port = dmx.select_port()

# Super boiled down
def render_frame(brightness, red, green, blue):
	
	light_dmx_id = 10;
	
	# BETOPPER LC200W-H light fixture DMX config as an example
	port.dmx_frame[light_dmx_id] = brightness	# shutter
	port.dmx_frame[light_dmx_id+1] = 0  			# ?
	port.dmx_frame[light_dmx_id+2] = 0 				# ?
	port.dmx_frame[light_dmx_id+3] = 0 				# ?
	port.dmx_frame[light_dmx_id+4] = red 			# red
	port.dmx_frame[light_dmx_id+5] = green		# green
	port.dmx_frame[light_dmx_id+6] = blue 		# blue

	print(brightness, red, green, blue)

	port.render()


# Example loop
while True:

	red = randint(0,255)
	green = randint(0,255)
	blue = randint(0,255)
	brightness = 150

	render_frame(red, green, blue, brightness)