# lioness
Lioness is a command line Python 2.7 interface for communicating with Extron IPL Controllers

# How to use
Lioness is invoked like so:

  lioness.py 127.0.0.1 command command command command
  
It supports passing multiple commands to the same IPL controller. 
 
# What are the commands?
If, like myself, you're looking to try and find out what on earth the 'commands' actually are, then this may help you.
This was originally developed as part of an in house tool for an educational institution. After spending a while reading the documentation for the Extron IPL 250 I decided it may be easier for me to just go digging myself. I fired up the GlobalViewer control panel in a web browser and started sniffing my traffic with WireShark. I noticed that the GlobalViewer ActiveX control was communicating with the IPL 250 via telnet. So after some further digging, I noticed that it was sending control commands such as "W1,2,136LE|". 

Once I recognised the format of these commands, further digging revealed a bunch of XML files stored on the IPL 250 itself. These XML files accurately described every operation and value available to the GlobalViewer interface, and its respective command code. Every operation to get a value or perform an action can be achieved by sending these "W1,2,136LE|" style command codes. All of which are documented in the XML files on the IPL 250.
