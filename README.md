# mindstorms-vll
Several methods to control LEGO Code Pilot and MicroScout with VLL


The LEGO Code Pilot was the first LEGO pBrick (programmable brick), the first member of the MINDSTORMS familly.

It could receive and store "instructions" through a optical input. The set came with a laminated A3 paper, the "Code Pilot Bar Code Sheet" containing code bars of the available instructions. A later set, the Scout, could also send these instructions by flashing a LED. Another pBrick, the MicroScout, could also receive these instructions. A common method to connect the Scout to the MicroScout was through an optic fiber link.

The RCX SDK included the details of the VLL language and it was possible to use the RCX output with a lamp to generate VLL codes.

Since the EV3 can also control a light, I decided to use it to control the Code Pilot and the MicroScout. After first success I tryed other methods.

1. EV3 output port with NXT-RCX adapter and Power Functions Light

In ev3dev configure the output port to led mode and use the 'vll-outa.py' script

(still to document)

2. EV3 status LED

3. USB FTDI adapter in bitbang mode and a LED (works with ev3dev, linux laptop and Raspberry Pi, probably also with Windows and OSX)

4. Arduino (NodeMCU) and a LED connected to a GPIO pin

5. Raspberry Pi and a LED conencted to a GPIO pin


An interesting discovery: although the LEGO optical fiber (~21L length) barelly works, a TOSLink optical fiber (1.2 meters or 4 feet) works fine, allowing better distances. And it connects very well to LEGO bricks.
