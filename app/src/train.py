import face_recognition as fr
import os
import pickle  # For saving encodings
import cv2

# import matplotlib.pyplot as plt

# Define paths to your image directory and output file
def train():
    #image_dir have the path of the directry that contain the traning data

    image_dir = os.path.join(os.getcwd(),"app","data", "training")
    # person holds the data have the folders in it
    persons = os.listdir(image_dir)  # Replace with your actual directory

    output_file = os.path.join(os.getcwd(),"app", "data", "saved", "encodings.pickle") # if not present in the dir it will create it automatically

    # Create an empty list to store known face encodings and names
    
    known_face_encodings = []
    known_face_names = []

    # Loop through each image in the directory
    for person_dir in persons:
        # Load the image
        print(f"Training Data for '{person_dir}'")
        for filename in os.listdir(os.path.join(image_dir,person_dir)):
            filename = os.path.join(image_dir, person_dir, filename)
            image = cv2.imread(filename)
            # image = fr.load_image_file(os.path.join(image_dir, filename))
        # Convert the image to RGB format (assuming it's BGR)
            rgb_image = image[:, :, ::-1]
            # small_rgb_image = rgb_image#cv2.resize(rgb_image, (0, 0), fx=0.25, fy=0.25)
            small_rgb_image = cv2.resize(rgb_image, (0, 0), fx=0.25, fy=0.25)
            # rgb_image = cv2.COLOR_BGR2RGB(image)
            # Find all faces in the image
            print(f"Finding face locations in '{filename}'")
            face_locations = fr.face_locations(small_rgb_image)
            name = person_dir #os.path.dirname(person_dir)
            # Check if there are any faces detecte
            print(face_locations)
            # continue
            if face_locations:
                # Encode the face from the first location (assuming there's only one person)
                face_encoding = fr.face_encodings(small_rgb_image, face_locations)[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(name)
            else:
                print(f"No face detected in image: {filename}")

    # Save the known face encodings and names to a file
    data = (known_face_encodings, known_face_names)
    # print(data)
    with open(output_file, 'wb') as f:
        pickle.dump(data, f)

    print("Encodings saved to", output_file)
