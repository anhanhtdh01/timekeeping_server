import mtcnn
import cv2


class FaceDetector:
    def __init__(self):
        self.detector = mtcnn.MTCNN()

    def detect(self, img):
        faces = self.detector.detect_faces(img)
        return faces

    def find_max_face(self, img):
        faces = self.detector.detect_faces(img)

        if len(faces) == 0:
            return None
        else:
            biggest_face = faces[0]
            max_area = biggest_face["box"][2] * biggest_face["box"][3]
            for face in faces:
                area = face["box"][2] * face["box"][3]
                if area > max_area:
                    max_area = area
                    biggest_face = face
        return biggest_face


if __name__ == "__main__":

    # cap = cv2.VideoCapture(0)
    # while True:
        # __, frame = cap.read()
    detector = FaceDetector()

    img_path = "test_3.jpg"
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    img = cv2.imread(img_path)
    # img = cv2.resize(img, dsize= None, fx=0.25, fy=0.25)

    # Detect all face
    print("\n\n\nDETECT ALL FACES")
    faces = detector.detect(img)
    print('\n', faces)

    # Tìm khuôn mặt lớn nhất
    print('\n\n\nDETECT MAX FACE')
    biggest_face = detector.find_max_face(img)
    if biggest_face == None:
        print("\nDon't detect face...")
    else:
        bbox = biggest_face["box"]
        land_mark_mtcnn = biggest_face["keypoints"]
        landmark = {'left_eye': land_mark_mtcnn['left_eye'], 'right_eye': land_mark_mtcnn['right_eye'],
                    'nose': land_mark_mtcnn['nose'], 'mouth_left': land_mark_mtcnn['mouth_left'],
                    'mouth_right': land_mark_mtcnn['mouth_right']}

        cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 2)
        cv2.imshow("biggest_face", img)
        cv2.waitKey()

        print("\nLandmark 5 points: ", landmark)
        print('\nBBox: ', bbox)

    # cap.release()
    cv2.destroyAllWindows()