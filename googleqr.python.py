import pyqrcode
import png
from pyqrcode import QRCode

site="www.google.com"

url_qr=pyqrcode.create(site)

url_qr.png("google.png",scale=8)
