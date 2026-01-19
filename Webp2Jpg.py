import os
import platform
from PIL import Image


system = platform.system()
if system == "Windows":
    picturesFolder = os.path.expanduser(r"~\Pictures")

elif system == "Darwin":
    picturesFolder = os.path.expanduser("~/Downloads")

elif system == "Linux":
    picturesFolder = os.path.expanduser("~/Downloads")

else:
    raise RuntimeError("Unsupported operating system")


def is_webp(file_path):
    # Check if the file extension is .webp
    if file_path.lower().endswith('.webp'):
        return True

    # Check if the file is of type WEBP
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
            base_name = os.path.splitext(file_path)[0]
            jpg_path = base_name + ".jpg"
            img.save(jpg_path, "JPEG")
            os.remove(file_path)
            print(f"Converted: {file_path}")

    except Exception as e:
        print(f"Error converting {file_path}: {e}")


if __name__ == "__main__":
    if os.path.exists(picturesFolder):
        for root, _, files in os.walk(picturesFolder):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if is_webp(file_path):
                    convert_to_jpg(file_path)
    else:
        print("Folder does not exist!")
