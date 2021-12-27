import requests
import base64
import cv2


# Gets the contents of an image on the Internet to be
# sent to the machine learning model for classifying
def getDataFromUrl(wwwLocationOfImage):
  data = requests.get(wwwLocationOfImage).content
  return base64.b64encode(data).decode()


# Gets an image from the webcam
def getDataFromWebcam():
  cam = cv2.VideoCapture(0)
  try:
    ok, image = cam.read()
    if ok != True:
      raise ValueError("Problem using the webcam")
    ok, data = cv2.imencode(".jpg", image)
    if ok != True:
      raise ValueError("Problem getting image data")
    return base64.b64encode(data).decode()
  finally:
    cam.release()


# Gets the contents of an image file to be sent to the
# machine learning model for classifying
def getDataFromFile(locationOfImageFile):
  with open(locationOfImageFile, "rb") as f:
    data = f.read()
    return base64.b64encode(data).decode()