from PIL import Image, ImageFilter
import os

input_folder = f"inp1"

output_folder = f"outp"

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        filtered_image = image.filter(ImageFilter.BLUR)

        base_name, extension = os.path.splitext(filename)
        new_filename = f"{base_name}_filtered{extension}"
        output_path = os.path.join(output_folder, new_filename)

        filtered_image.save(output_path)
