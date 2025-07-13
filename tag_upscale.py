from PIL import Image
import os
import glob

def upscale_and_pad_images(directory='./', scale_factor=5, padding=5):
    # Find all PNG files in the directory and subdirectories
    png_files = glob.glob(os.path.join(directory, "**", "*.png"), recursive=True)

    if not png_files:
        print(f"No PNG files found in {os.path.abspath(directory)} or its subdirectories")
        return

    for image_path in png_files:
        # Open the image
        img = Image.open(image_path)

        # Get original dimensions
        width, height = img.size

        # Upscale the image
        new_width = width * scale_factor
        new_height = height * scale_factor
        upscaled_img = img.resize((new_width, new_height), Image.Resampling.NEAREST)

        # Create a new image with padding
        padded_img = Image.new(upscaled_img.mode,
                              (new_width + 2*padding, new_height + 2*padding),
                              (255, 255, 255))  # White background

        # Paste the upscaled image onto the padded canvas
        padded_img.paste(upscaled_img, (padding, padding))

        # Save the result
        padded_img.save(image_path)
        print(f"Processed: {image_path}")

    print(f"Finished processing {len(png_files)} images.")

if __name__ == "__main__":
    upscale_and_pad_images()
