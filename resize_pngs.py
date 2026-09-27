import os
from PIL import Image

INPUT_FOLDER_PATH = input("Input folder (input_images): ") or "input_images"
TARGET_WIDTH = int(input("Pixel size: "))
OUTPUT_FOLDER_NAME = "resized"

def get_png_files(folder):
    return [f for f in os.listdir(folder) if f.lower().endswith(".png")]

def resize_image(src_path, dst_path, width):
    with Image.open(src_path) as img:
        if img.width == width:
            img.save(dst_path)
            return
        ratio = width / float(img.width)
        height = round(img.height * ratio)
        resized = img.resize((width, height), Image.LANCZOS)
        resized.save(dst_path)

def process_folder(folder, width):
    files = get_png_files(folder)
    if not files:
        print("No PNG files found in the folder.")
        return
    output_folder = os.path.join(folder, OUTPUT_FOLDER_NAME)
    os.makedirs(output_folder, exist_ok=True)
    for filename in files:
        src_path = os.path.join(folder, filename)
        dst_path = os.path.join(output_folder, filename)
        try:
            resize_image(src_path, dst_path, width)
            print(f"Resized: {filename}")
        except Exception as e:
            print(f"Failed to resize {filename}: {e}")

if __name__ == "__main__":
    process_folder(INPUT_FOLDER_PATH, TARGET_WIDTH)
