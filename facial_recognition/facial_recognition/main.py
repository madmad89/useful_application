import os
import cv2
import pandas as pd
from deepface import DeepFace


class PictureCapture:
    def __init__(self, save_directory='pictures'):
        self.save_directory = save_directory

    def capture_and_save(self, name):
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        save_path = os.path.join(self.save_directory, f"{name}.png")
        cv2.imwrite(save_path, frame)
        capture.release()
        cv2.destroyAllWindows()
        return save_path


def web_capture():
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    cv2.imwrite('capture.png', frame)
    # When everything done, release the capture
    capture.release()
    cv2.destroyAllWindows()


def people_analyzer(analyze_result: dict):
    for file in os.listdir('pictures'):
        result = DeepFace.analyze(img_path=f'pictures/{file}',
                                  actions=('age', 'gender', 'race', 'emotion'))
        analyze_result['name'].append(os.path.splitext(file)[0])
        analyze_result['age'].append(result[0]['age'])
        analyze_result['gender'].append(result[0]['dominant_gender'])
        analyze_result['race'].append(result[0]['dominant_race'])
        analyze_result['emotions'].append(result[0]['dominant_emotion'])

    df = pd.DataFrame(analyze_result)
    df.to_csv('image_details.csv')
    return df


capture = PictureCapture()
picture_path = capture.capture_and_save(input(str('Input your name: ')))
print(f"Picture saved at: {picture_path}")

if __name__ == '__main__':
    analyze_result = {
        'name': [],
        'age': [],
        'gender': [],
        'race': [],
        'emotions': []
    }
    people_analyzer(analyze_result)

    web_capture()
    obj = DeepFace.verify(img1_path="pictures/Madalin.png",
                          img2_path="capture.png",
                          model_name='VGG-Face'
                          )
    print(obj)
    if obj['verified']:
        print(f'{picture_path} Welcome!')
    else:
        print('not you!')
