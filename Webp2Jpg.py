import os
from PIL import Image

def is_webp(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format == "WEBP"
    except Exception:
        return False

def convert_to_jpg(file_path):
    try:
        with Image.open(file_path) as img:
            # Ensure RGB mode
            if img.mode != "RGB":
                img = img.convert("RGB")
            
            # Save as JPG
            img.save(file_path, "JPEG")
            print(f"Converted: {file_path}")
    except Exception as e:
        print(f"Error converting {file_path}: {e}")

if __name__ == "__main__":
    """ Absolute URL to folder goes here"""
    picturesFolder = "C:\\Users\\MUTRA\\Pictures"

    if os.path.exists(picturesFolder):
        for root, _, files in os.walk(picturesFolder):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if is_webp(file_path):
                    convert_to_jpg(file_path)
    else:
        print("Folder does not exist!")