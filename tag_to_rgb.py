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
    """Convert image to RGB and make transparent pixels white."""
    img = Image.open(image_path)

    # Check if the image has transparency
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        # Create a white background image
        background = Image.new('RGB', img.size, (255, 255, 255))

        # Paste the image on the background, using the alpha channel as mask
        if img.mode == 'RGBA':
            background.paste(img, (0, 0), img)
        else:
            # Convert to RGBA first if needed
            img_rgba = img.convert('RGBA')
            background.paste(img_rgba, (0, 0), img_rgba)

        # Save the result, overwriting the original
        background.save(image_path)
        print(f"Processed {image_path}")
    elif img.mode != 'RGB':
        # If image doesn't have transparency but is not RGB, convert it
        img_rgb = img.convert('RGB')
        img_rgb.save(image_path)
        print(f"Converted {image_path} to RGB")

def main():
    directory = "./"  # Change this to the directory containing your PNG files
    png_files = find_png_files(directory)
    print(f"Found {len(png_files)} PNG files")

    for png_file in png_files:
        process_image(png_file)

    print("Processing complete!")

if __name__ == "__main__":
    main()
