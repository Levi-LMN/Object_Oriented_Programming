import face_recognition
import cv2

# Load the image with the known face (Levi's image)
known_image = face_recognition.load_image_file("levi.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Load the group photo (Fahm's image)
group_image = face_recognition.load_image_file("fahm.jpg")
face_locations = face_recognition.face_locations(group_image)
face_encodings = face_recognition.face_encodings(group_image, face_locations)

# Compare the face in the group photo with the known face
for face_encoding in face_encodings:
    # Compare the face encodings
    results = face_recognition.compare_faces([known_face_encoding], face_encoding)
    
    if results[0]:
        print("Match found! This is the same person.")
    else:
        print("No match found.")

# Display the group photo with rectangles around detected faces
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(group_image, (left, top), (right, bottom), (0, 0, 255), 2)

cv2.imshow("Group Photo with Face Recognition", group_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
