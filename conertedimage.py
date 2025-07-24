from PIL import Image
import os

# Dataset folder path
dataset_path = "datasetface"

def convert_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Ensure it's in RGB and not corrupted
            rgb_image = img.convert("RGB")
            rgb_image.save(output_path, format="JPEG", quality=95)
            print(f"✅ Converted: {output_path}")
    except Exception as e:
        print(f"❌ Error converting {input_path}: {e}")

# Loop through all subfolders and images
for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    for file in os.listdir(person_path):
        input_file_path = os.path.join(person_path, file)

        # Skip if not a file or already converted
        if not os.path.isfile(input_file_path) or file.endswith("_converted.jpg"):
            continue

        # New converted image path
        new_filename = os.path.splitext(file)[0] + "_converted.jpg"
        output_file_path = os.path.join(person_path, new_filename)

        convert_image(input_file_path, output_file_path)
