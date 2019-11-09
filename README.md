# qr_pil
QR code encoder for Python Pillow

Made by walking through [this tutorial](https://www.thonky.com/qr-code-tutorial/) on how QR code encoding works.

This module will __only generate QR codes in byte mode__ no matter what input data is given. Use another library if you want to use other modes like ECI or alphanumeric.

### Dependencies
- [reedsolo](https://pypi.org/project/reedsolo/) for Reed-Solomon error correction
- [Pillow](https://pypi.org/project/Pillow/) for making images
- [numpy](https://pypi.org/project/numpy/) and [bitstream](https://pypi.org/project/bitstream/) for easy to use binary streams.

### Example
Saves a "Hello world!" QR code as "output.png" and opens it with Pillow

```py
from qr_pil import QRCode

qr = QRCode("Hello world!")
image = qr.toImage()
image.save("output.png", "PNG")
image.show()
```
