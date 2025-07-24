import os
import face_recognition
import pickle

# Dataset folder path
dataset_path = "datasetface"

# Store encodings and names
known_encodings = []
known_names = []

# Loop through all people in dataset
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_folder):
        continue

    # Loop through each converted image of the person
    for image_name in os.listdir(person_folder):
        # Use only converted JPG files
        if not image_name.endswith("_converted.jpg"):
            continue

        image_path = os.path.join(person_folder, image_name)

        try:
            # Load image
            image = face_recognition.load_image_file(image_path)

            # Get face encodings
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(person_name)
                print(f"✅ Encoded: {image_name}")
            else:
                print(f"⚠️ No face found in {image_name}")

        except Exception as e:
            print(f"❌ Error with image {image_name}: {e}")

# Save encodings to a pickle file
data = {"encodings": known_encodings, "names": known_names}

# Create encodings folder if not exists
os.makedirs("encodings", exist_ok=True)

# Save to file
with open("encodings/face_encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("✅ All face encodings saved successfully.")
