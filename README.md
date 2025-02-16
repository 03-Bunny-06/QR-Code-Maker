# QR Maker: A Simple QR Code Generator for Images and UPI

## Project Description

QR Maker is a Python-based utility to create QR codes from image URLs or UPI IDs. This project offers a simple interface to generate QR codes for personal or professional use, with customization options like unique names and color schemes.

## Features

- **Image to QR Code**: Converts an image URL into a QR code.
- **UPI to QR Code**: Generates a QR code for UPI payment links.
- **Customization**: Allows setting unique names for QR code files and adjusts color schemes for better visibility.

## Prerequisites

Ensure you have Python installed on your system. Additionally, install the required library by running:

```sh
pip install qrcode[pil]
```

## How to Run

1. Clone the repository or download the script file.
2. Open a terminal/command prompt and navigate to the project directory.
3. Run the script using:

```sh
python qr_maker.py
```

## Usage Instructions

### Choose an Option
- **Option 1**: Generate a QR code for an image URL.
- **Option 2**: Generate a QR code for a UPI ID.

### Image to QR Code
1. Enter the URL of the image you want to encode.
2. Provide a custom name for the QR code file.
3. The QR code will be generated, displayed, and saved as `<custom_name>.png`.

### UPI to QR Code
1. Enter your UPI ID (e.g., `example@upi`).
2. Provide a custom name for the QR code file.
3. The QR code will be generated, displayed, and saved as `<custom_name>.png`.

## Example Walkthrough

### Image to QR Code
#### **Input:**
```
Image URL: https://example.com/image.jpg
Custom name: my_image_qr
```
#### **Output:**
- A QR code with a green foreground and black background is displayed and saved as `my_image_qr.png`.

### UPI to QR Code
#### **Input:**
```
UPI ID: example@upi
Custom name: my_upi_qr
```
#### **Output:**
- A QR code with a white foreground and black background is displayed and saved as `my_upi_qr.png`.

## Customization

The QR code styles can be customized by modifying:

- **Fill Color**: Change the `fill_color` parameter in the `make_image` method.
- **Background Color**: Change the `back_color` parameter in the `make_image` method.

## Code Overview

The script has three main functions:

- `options()`: Displays a menu to choose between the two functionalities.
- `image_qr()`: Handles QR code generation for image URLs.
- `upi_qr()`: Handles QR code generation for UPI IDs.

![Orange Modern Attractive YouTube Thumbnail](https://github.com/user-attachments/assets/e7b78a98-5389-4016-bf9e-884726a55dfa)

![Orange Modern Attractive YouTube Thumbnail (1)](https://github.com/user-attachments/assets/ccc4fa0c-f080-4583-8cfb-00ebf6c0478a)


