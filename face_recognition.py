import cv2
import dlib
import face_recognition

known_image = face_recognition.load_image_file("known.jpg")
known_image_encoding = face_recognition.face_encodings(known_image)[0]

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    if ret:
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        for face_encoding in face_encodings:
            results = face_recognition.compare_faces([known_image_encoding], face_encoding)
            name="unknown"

            if results[0]:
                name="known"
                first_match_index = results.index(True)
            
            top,right,bottom,left=face_locations[0]
            cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
            cv2.putText(frame,name,(left,top-6),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1,cv2.LINE_AA)
 
        cv2.imshow('Video', frame)

    else:
        print("Error reading frame")
        break
    
    #按q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()