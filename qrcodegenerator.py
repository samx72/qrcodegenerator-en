# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
input = input("enter url: ")
# String which represents the QR code
s = input
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"

  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)