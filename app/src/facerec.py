import face_recognition
from ..globals import GLOBAL

class FaceRead:
    def __init__(self) -> None:
        GLOBAL['facerec']=self
    def rec_face(frame, known_face_encodings, known_face_names):
        rgb_frame = frame

        # Find all faces in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)

        # Identify faces from known encodings
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # Compare against known face encodings
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match is found, get the name
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

        return face_locations, face_names
    
def rec_face(frame, known_face_encodings, known_face_names):
        rgb_frame = frame

        # Find all faces in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)

        # Identify faces from known encodings
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # Compare against known face encodings
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            # by defult the match will return false 
            
            name = "Unknown"

            # If a match is found, get the name
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

        return face_locations, face_names