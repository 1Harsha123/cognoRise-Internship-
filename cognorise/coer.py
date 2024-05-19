import qrcode
import cv2
import numpy as np
from PIL import Image

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

def decode_qr_code(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    
    if bbox is not None:
        print(f"QR code data: {data}")
    else:
        print("QR code not detected")
        
    return data

if __name__ == "__main__":
    # Generate a QR code
    data = "https://www.example.com"
    filename = "example_qr.png"
    generate_qr_code(data, filename)
    
    # Decode the generated QR code
    decoded_data = decode_qr_code(filename)
