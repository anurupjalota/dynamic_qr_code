import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = "https://anurupjalota.github.io/dynamic_qr_code/try1.pdf"
  
# Generate QR code 
url = pyqrcode.create(s) 
  

url.png('myqr.png', scale = 6) 