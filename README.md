**QR Maker: A Simple QR Code Generator for Images and UPI**

Project Description:

QR Maker is a Python-based utility to create QR codes from image URLs or UPI IDs. This project offers a simple interface to generate QR codes for personal or professional use, with customization options like unique names and color schemes.

<hr/>

Features:

* Image to QR Code: Converts an image URL into a QR code.
* UPI to QR Code: Generates a QR code for UPI payment links.
* Customization: Allows setting unique names for QR code files and adjusts color schemes for better visibility.

<hr/>

Prerequisites:

* Ensure you have Python installed on your system. Additionally, install the required library by running: pip install qrcode[pil]

<hr/>

How to Run:

1. Clone the repository or download the script file.
2. Open a terminal/command prompt and navigate to the project directory.
3. Run the script using: python qr_maker.py

<hr/>

Usage Instructions:

1. Choose an Option
* Option 1: Generate a QR code for an image URL.
* Option 2: Generate a QR code for a UPI ID.
2. Image to QR Code
* Enter the URL of the image you want to encode.
* Provide a custom name for the QR code file.
* The QR code will be generated, displayed, and saved as <custom_name>.png.
3. UPI to QR Code
* Enter your UPI ID (e.g., example@upi).
* Provide a custom name for the QR code file.
* The QR code will be generated, displayed, and saved as <custom_name>.png.

<hr/>

Example Walkthrough:

Image to QR Code
1. Input:
* Image URL: https://example.com/image.jpg
* Custom name: my_image_qr

2. Output:
* A QR code with green foreground and black background is displayed and saved as my_image_qr.png.

UPI to QR Code
1. Input:
* UPI ID: example@upi
* Custom name: my_upi_qr
2. Output:
* A QR code with white foreground and black background is displayed and saved as my_upi_qr.png.

<hr/>

Customization:

The QR code styles can be customized by modifying:
* Fill Color: Change the fill_color parameter in the make_image method.
* Background Color: Change the back_color parameter in the make_image method.

<hr/>

Code Overview:

The script has three main functions:
1. options(): Displays a menu to choose between the two functionalities.
2. image_qr(): Handles QR code generation for image URLs.
3. upi_qr(): Handles QR code generation for UPI IDs.
