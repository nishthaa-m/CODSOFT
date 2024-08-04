#Face Detection+Recognition

import cv2
import face_recognition

# Load known faces and their names
def load_known_faces():

    known_faces = []
    known_names = []

    # Adding paths to images of known people
    image_files = {
        "Person A": "Images/A._P._J._Abdul_Kalam.jpg",
        "Person B": "Images/Lata Mangeshkar.jpg",
        "Person C": "Images/Sachin_Tendulkar.jpg"
    }

    for name, image_file in image_files.items():
        image = face_recognition.load_image_file(image_file)
        encodings = face_recognition.face_encodings(image)
        
        if encodings:
            encoding = encodings[0]
            known_faces.append(encoding)
            known_names.append(name)
        else:
            print(f"No faces found in the image {image_file}. Skipping this file.")
    
    return known_faces, known_names

def recognize_faces(frame, known_faces, known_names):
    # Finding all face locations and face encodings in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        
        # Checking if there is a match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
        
        names.append(name)
    
    return face_locations, names

def main():
    known_faces, known_names = load_known_faces()
    
    # Initialize video capture (0 for default camera)
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
        face_locations, names = recognize_faces(rgb_frame, known_faces, known_names)

        for (top, right, bottom, left), name in zip(face_locations, names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the capture and close windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
