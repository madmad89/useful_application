import cv2
import os


class PictureCapture:
    def __init__(self, save_directory='pictures'):
        self.save_directory = save_directory

    def capture_and_save(self, name):
        # Open the video capture device
        capture = cv2.VideoCapture(0)
        # Read a frame from the capture device
        ret, frame = capture.read()
        # Define the save path for the captured picture
        save_path = os.path.join(self.save_directory, "example.jpg")
        # Save the frame as an image at the specified save path
        cv2.imwrite(save_path, frame)
        # When everything done,Release the capture device
        capture.release()
        # Close all windows created by OpenCV
        cv2.destroyAllWindows()
        # Return the save path of the captured picture
        return save_path


capture = PictureCapture()
picture_path = capture.capture_and_save("example")
print(f"Picture saved at: {picture_path}")

# Create Classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

# Read image, Convert to Grayscale, Run Classifier
image = cv2.imread('pictures/example.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face = face_classifier.detectMultiScale(image_gray, 1.1, 4)

# Create Rectangles
for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
    roi_gray = image_gray[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)

# Show Finale Image
cv2.imshow('img', image)
cv2.waitKey()


# Module used from:
# github.com/opencv/opencvblob/master/data/haarcascades/
# haarcascade_frontalface_default.xml
# haarcascade_eye.xml
