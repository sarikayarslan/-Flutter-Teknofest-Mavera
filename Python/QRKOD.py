import cv2
import numpy as np
from pyzbar.pyzbar import decode
import numpy as np
import requests
import telebot
from firebase import firebase
import pyrebase
fb = firebase.FirebaseApplication("https://mavera-31c55-default-rtdb.firebaseio.com/",None)
Bot_Token = "1768779123:AAGNIXpXXH0fNBunc4rTZIyhQRH51SEvUXk"  # Bot Token Tanımlaması
Chat_ID = "862411997"  # Chat ID Tanımlaması
KekikPython = telebot.TeleBot(Bot_Token)
def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "HES  :" + str(barcodeData)

        DataForLink = {'text' : string}
        requests.post("https://api.telegram.org/bot" + Bot_Token +
                      "/sendMessage?chat_id=" + Chat_ID,
                      data=DataForLink)

        cv2.putText(frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        print("HES KODU: " + barcodeData + " | Type: " + barcodeType)
       # y =[str(barcodeData)]
        hessplit=barcodeData.split("|")
        result = fb.put("User", "HES", hessplit[1])
        print(hessplit[1])

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break