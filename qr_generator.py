import qrcode
import qrcode.constants

def options():
    print('Welcome to the QR Maker.\n1. Image to QR Code\n2. UPI ID to QR Code')
    select = input('Enter the option(1/2): ')
    if select == '1':
        image_qr()
    elif select == '2':
        upi_qr()
    else:
        print('Enter a valid choice.')
    
def image_qr():
    image_url = input('Enter the image address: ')
    image_name = input('Enter your custom image name: ')

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=5
    )

    qr.add_data(image_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color= 'green', back_color='black')
    img.show()
    img.save(f'{image_name}.png')

def upi_qr():
    upi_id = input('Enter your UPI ID: ')
    upi_name = input('Enter the custom UPI ID name: ')
    upi_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=5
    )

    qr.add_data(upi_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color='white', back_color='black')
    img.save(f'{upi_name}.png')
    img.show()

options()