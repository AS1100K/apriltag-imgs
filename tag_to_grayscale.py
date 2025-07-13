import os
from PIL import Image

def find_png_files(directory):
    """Find all PNG files in a directory and its subdirectories."""
    png_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                png_files.append(os.path.join(root, file))
    return png_files

def process_image(image_path):
    """Convert image to grayscale, regardless of original format."""
    try:
        img = Image.open(image_path)

        # Convert to grayscale
        img_gray = img.convert('L')

        # Save the grayscale image, overwriting the original
        img_gray.save(image_path)
        print(f"Converted {image_path} to grayscale")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def main():
    directory = "./"  # Current directory - change if needed
    png_files = find_png_files(directory)
    print(f"Found {len(png_files)} PNG files")

    for png_file in png_files:
        process_image(png_file)

    print("Conversion to grayscale complete!")

if __name__ == "__main__":
    main()
