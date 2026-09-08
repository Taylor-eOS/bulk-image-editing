from PIL import Image
import os

folder_path = input("Input folder: ")
target_width = int(input("Pixel size: "))

def get_png_files(folder):
    return [f for f in os.listdir(folder) if f.lower().endswith(".png")]

def resize_image(path, width):
    with Image.open(path) as img:
        if img.width == width:
            return
        ratio = width / float(img.width)
        height = round(img.height * ratio)
        resized = img.resize((width, height), Image.LANCZOS)
        resized.save(path)

def process_folder(folder, width):
    files = get_png_files(folder)
    if not files:
        print("No PNG files found in the folder.")
        return
    for filename in files:
        full_path = os.path.join(folder, filename)
        try:
            resize_image(full_path, width)
            print(f"Resized: {filename}")
        except Exception as e:
            print(f"Failed to resize {filename}: {e}")

if __name__ == "__main__":
    process_folder(folder_path, target_width)
