import os
import cv2
import pandas as pd
from deepface import DeepFace


class PictureCapture:
    def __init__(self, save_directory='pictures'):
        self.save_directory = save_directory

    def capture_and_save(self, name):
        # Open the video capture device
        capture = cv2.VideoCapture(0)
        # Read a frame from the capture device
        ret, frame = capture.read()
        # Define the save path for the captured picture
        save_path = os.path.join(self.save_directory, f"{name}.png")
        # Save the frame as an image at the specified save path
        cv2.imwrite(save_path, frame)
        # When everything done,Release the capture device
        capture.release()
        # Close all windows created by OpenCV
        cv2.destroyAllWindows()
        # Return the save path of the captured picture
        return save_path


def web_capture():
    # Open the video capture device
    capture = cv2.VideoCapture(0)
    # Read a frame from the capture device
    ret, frame = capture.read()
    # Save the frame as an image with the name 'capture.png'
    cv2.imwrite('capture.png', frame)
    # Release the capture device
    capture.release()
    # Close all windows created by OpenCV
    cv2.destroyAllWindows()


def people_analyzer(analyze_result: dict):
    # Iterate over files in the 'pictures' directory
    for file in os.listdir('pictures'):
        # Analyze the face in the image using DeepFace library
        result = DeepFace.analyze(img_path=f'pictures/{file}', actions=('age', 'gender', 'race', 'emotion'))
        # Append the name, age, gender, race, and dominant emotion to the analyze_result dictionary
        analyze_result['name'].append(os.path.splitext(file)[0])
        analyze_result['age'].append(result[0]['age'])
        analyze_result['gender'].append(result[0]['dominant_gender'])
        analyze_result['race'].append(result[0]['dominant_race'])
        analyze_result['emotions'].append(result[0]['dominant_emotion'])

    # Create a DataFrame from the analyze_result dictionary
    df = pd.DataFrame(analyze_result)
    # Save the DataFrame as a CSV file named 'image_details.csv'
    df.to_csv('image_details.csv')
    # Return the DataFrame
    return df


# Create an instance of PictureCapture
capture = PictureCapture()
# Prompt the user to input their name and capture/save their picture
picture_path = capture.capture_and_save(input(str('Input your name: ')))
print(f"Picture saved at: {picture_path}")

if __name__ == '__main__':
    # Create an empty dictionary to store analysis results
    analyze_result = {
        'name': [],
        'age': [],
        'gender': [],
        'race': [],
        'emotions': []
    }
    # Analyze the pictures in the 'pictures' directory and store the results in the analyze_result dictionary
    people_analyzer(analyze_result)

    # Capture a picture from the webcam and save it as 'capture.png'
    web_capture()

    # Verify if the captured picture matches the saved picture using DeepFace library
    obj = DeepFace.verify(img1_path=picture_path,
                          img2_path="capture.png",
                          model_name='VGG-Face')
    print(obj)

    # Check if the pictures match and print the corresponding message
    if obj['verified']:
        print('Welcome!')
    else:
        print('You are not registered!')
