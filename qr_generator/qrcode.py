import frappe
import qrcode
from PIL import Image
import base64
from io import BytesIO
from datetime import datetime, timedelta  # Import the datetime and timedelta modules
import json  # Ensure json is imported


def get_qrcode(input_str):
    qr = qrcode.make(input_str)
    temp = BytesIO()
    qr.save(temp, "PNG")
    temp.seek(0)
    b64 = base64.b64encode(temp.read())
    return "data:image/png;base64,{0}".format(b64.decode("utf-8"))




@frappe.whitelist()
def generate_qr_code(data):
    """Generate a QR code and return the image as a base64 encoded string."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # Save the image in a BytesIO object
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Encode the image to base64
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    # Return the base64 string to use in the print format
    return img_base64








@frappe.whitelist()
def generate_qr_code_link(invoice_name):
    """Generate a QR code with the link to the invoice."""
    base_url = frappe.utils.get_url()  # Get the base URL of your site
    invoice_url = f"{base_url}/app/sales-invoice/{invoice_name}"  # URL to the specific invoice

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(invoice_url)  # Add the invoice URL to the QR code
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # Save the image in a BytesIO object
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Encode the image to base64
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    # Return the base64 string to use in the print format
    return img_base64






# generate multi fields in qrcode

import json  # Ensure json is imported

from datetime import datetime, time  # Ensure time is imported

# @frappe.whitelist()
# def generate_qr_code_for_invoice(invoice_name):
#     """Generate a QR code for the full invoice data and return the image as a base64 encoded string."""
#     # Fetch the invoice data
#     invoice = frappe.get_doc("Sales Invoice", invoice_name)
       
#     # Convert posting_time to a string if it's a time object
#     posting_time = invoice.posting_time.strftime("%H:%M:%S") if isinstance(invoice.posting_time, time) else str(invoice.posting_time)
    
#     # Create a dictionary of the relevant invoice fields
#     invoice_data = {
#         "Invoice Number": invoice.name,
#         "Customer": invoice.customer,
#         "Posting Date": invoice.posting_date.strftime("%Y-%m-%d"),
#         "Posting Time": posting_time,  # Handle time object
#         "Grand Total": invoice.grand_total,
#         "Currency": invoice.currency
#     }
    
#     # Convert the dictionary to JSON
#     data = json.dumps(invoice_data, ensure_ascii=False)
    
#     # Generate the QR code
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)

#     img = qr.make_image(fill="black", back_color="white")

#     # Save the image in a BytesIO object
#     img_bytes = BytesIO()
#     img.save(img_bytes, format="PNG")
#     img_bytes.seek(0)

#     # Encode the image to base64
#     img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

#     # Return the base64 string to use in the print format
#     return img_base64


#test1111111111111111111111111111111111111111111111111111111111111111
@frappe.whitelist()
def generate_qr_code_for_invoice(data):
    """Generate a QR code for the full invoice data and return the image as a base64 encoded string."""
    # Fetch the invoice data
    invoice = frappe.get_doc("Sales Invoice", data)
       
    # Convert posting_time to a string if it's a time object
    posting_time = invoice.posting_time.strftime("%H:%M:%S") if isinstance(invoice.posting_time, time) else str(invoice.posting_time)
    
    # Create a dictionary of the relevant invoice fields
    invoice_data = {
        "Invoice Number": invoice.company,
        "Customer": invoice.tax_id,
        "Posting Date": invoice.posting_date.strftime("%Y-%m-%d"),
        "Posting Time": posting_time, 
        "Grand Total": invoice.grand_total,
        "Total Taxes": invoice.total_taxes_and_charges
    }
    
    # Convert the dictionary to JSON
    data = json.dumps(invoice_data, ensure_ascii=False)
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # Save the image in a BytesIO object
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Encode the image to base64
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    # Return the base64 string to use in the print format
    return img_base64



###############3




@frappe.whitelist()
def generate_qr_code_link_pdf(invoice_name):
    """Generate a QR code with the link to the PDF file of the invoice."""
    base_url = frappe.utils.get_url()  # Get the base URL of your site
    pdf_url = f"{base_url}/api/method/frappe.utils.print_format.download_pdf?doctype=Sales%20Invoice&name={invoice_name}&format=Standard&no_letterhead=0"  # URL to the PDF file of the invoice

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(pdf_url)  # Add the PDF URL to the QR code
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # Save the image in a BytesIO object
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Encode the image to base64
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    # Return the base64 string to use in the print format
    return img_base64