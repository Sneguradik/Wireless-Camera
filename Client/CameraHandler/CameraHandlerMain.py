import threading as th
from unittest.loader import _SortComparisonMethod
import cv2
from imutils.video import VideoStream
import mediapipe as mp

class DeamonCapturing():
    def run(self):
        try:
            IsItPiCamera = True
            cap = VideoStream(src=0, usePiCamera=True, resolution=self.frameSize, framerate=32).start()
        except:
            IsItPiCamera = False
            cap = cv2.VideoCapture(0)

        detector = PoseDetector()
        
        while True:
            _ , img = cap.read()

            detector.findPose()
            lmlist = detector.getPosition(img)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

class PoseDetector():
    def __init__(self, mode= False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5) -> None:
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectionCon,self.trackCon)


    def findPose(self, img  , draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results =self.pose.process(img(imgRGB))
         
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def getPosition(self, img, draw=True):
        lmlist = []

        if self.results.pose_landmark:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0 , 0), cv2.FILLED)

def main():
    x = DeamonCapturing.run()

if __name__ == "__main__":
    main()