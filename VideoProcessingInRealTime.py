

import cv2

from modelAlphabet import loaded_model
from ImageProcessing import GetLmListFromImg




def RealTimeProcessing():
    cap = cv2.VideoCapture(0)
    #all bets
    y_classes = ["a", "b", "c", "ch", "e", "f", "g", "h", "i", "l", "m",
                 "n", "o", "p", "r", "sh", "t", "u", "v", "ya", "y",
                 "yu", "zh"]
    word:int


    while True:
        # Get image frame
        global mylmList
        success, img = cap.read()
        ret, fr = cap.read()

        if not success:
            pass
        # size = np.shape(fr)[0],np.shape(fr)[1]
        lmList1 = GetLmListFromImg(fr)

        try:
            prediction = loaded_model.predict(lmList1)
            print(prediction)

            for i in range(21):
                if prediction[0][i] > 0.5:
                    word = i
                else:
                    pass



            cv2.putText(img, y_classes[word], (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
        except Exception as e:
            cv2.putText(img, "There isn't your hand on the screen", (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        cv2.imshow("main", img)
        cv2.waitKey(1)
RealTimeProcessing()