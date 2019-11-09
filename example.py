#!/usr/bin/env python3
from qr_pil import QRCode

qr = QRCode("Hello world!")
image = qr.toImage()
image.save("output.png", "PNG")
image.show()
