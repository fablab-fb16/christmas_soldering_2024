import argparse
import sys
import os
from PIL import Image, ImageDraw, ImageFont
import subprocess
import shutil

# Constants for image dimensions
IMAGE_WIDTH = 696  # Example dimensions for label printer (pixels)
IMAGE_HEIGHT = 300

PRINTER_MODEL = "QL-800" # can also be specified via command line param

def check_prerequisites():
    """
    Perform initial checks for required packages, printers, etc.
    """
    # Check if `brother_ql` package is installed
    if not shutil.which("brother_ql"):
        sys.exit("Error: 'brother_ql' package is not installed or not in PATH. Install it using pip.")

    # Check for connected printers
    try:
        result = subprocess.run(["brother_ql", "discover"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0 or not result.stdout.strip():
            sys.exit(f"Error: No printers discovered. Make sure a compatible printer is connected.\nDetails: {result.stderr}")

        # Extract the printer identifier, removing junk after the underscore
        for line in result.stdout.strip().split("\n"):
            if "usb://" in line:
                printer_identifier = line.split("_")[0].strip()
                if printer_identifier:
                    return printer_identifier

        sys.exit("Error: No valid printer identifier found.")
    except Exception as e:
        sys.exit(f"Error during printer discovery: {e}")



def generate_image(text, image_path, width=696, height=300):
    """
    Generate a PNG image with the given text using modern Pillow methods.
    """
    try:
        # Create a blank white image
        img = Image.new('RGB', (width, height), color="white")
        draw = ImageDraw.Draw(img)

        # Use a default system font
        font = ImageFont.load_default(size=50)

        # Calculate text size using getbbox()
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Center the text
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2

        # Draw the text on the image
        draw.text((text_x, text_y), text, fill="black", font=font)
        img.save(image_path)
    except Exception as e:
        sys.exit(f"Error generating image: {e}")


def print_image(image_path, model, identifier):
    """
    Print the PNG image using the `brother_ql` command.
    """
    try:
        run_args = ["brother_ql", "-b", "pyusb", "-m", model, "-p", identifier, "print", "-l", "62", "--red", image_path]
        result = subprocess.run(
            run_args,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        if result.returncode != 0:
            sys.exit(f"Error priimage_pathnting image: {result.stderr}")
    except Exception as e:
        sys.exit(f"Error during printing: {e}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Print SSID and Password labels using a Brother QL printer.")
    parser.add_argument("ssid", nargs="?", help="SSID to print on the label")
    parser.add_argument("pw", nargs="?", help="Password to print on the label")
    parser.add_argument("-test", action="store_true", help="Generate and print a test label")
    parser.add_argument("-no_print", action="store_true", help="Disable Printing e.g. for debugging label creation")
    parser.add_argument("--model", default=PRINTER_MODEL, help="Printer model (default: QL-800)")
    parser.add_argument("--width", type=int, default=IMAGE_WIDTH, help="Width of the label image (default: 696)")
    parser.add_argument("--height", type=int, default=IMAGE_HEIGHT, help="Height of the label image (default: 300)")
    args = parser.parse_args()

    # Perform pre-checks
    if not args.no_print:
        printer_identifier = check_prerequisites()
        print("Printer found at " + printer_identifier)

    # Handle test mode
    if args.test:
        text = "Test Label\nBrother QL Printer"
    else:
        if not args.ssid or not args.pw:
            sys.exit("Error: SSID and Password must be provided unless in test mode.")
        text = f"SSID: {args.ssid}\nPassword: {args.pw}"

    # Generate and print the label
    # Determine script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define image path relative to the script's directory
    image_path = os.path.join(script_dir, "temp_label.png")
    #image_path = "temp_label.png"
    
    try:
        generate_image(text, image_path, width=args.width, height=args.height)
        if not args.no_print:
            print_image(image_path, args.model, printer_identifier)
            print("Label printed successfully.")
        else:
            print("No-Print Mode: no Label printed.")
    finally:
        if os.path.exists(image_path) and not args.no_print:
            os.remove(image_path)


if __name__ == "__main__":
    main()
