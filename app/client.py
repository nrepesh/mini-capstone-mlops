import base64
from pydantic import BaseModel
import requests
import cv2


def encode_image_data(img):
    """Encodes this frame as base64"""
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    _, img = cv2.imencode(".jpg", img)
    return base64.b64encode(img).decode("ascii")


def get_image():
    return(encode_image_data(cv2.imread("/home/nrepesh/MLOPS/mini-capstone-mlops/app/query_images/2.jpg")))


if __name__ == "__main__":
    query = {'id': 1,
             'b64img': get_image()
             }
    res = requests.post(f"http://35.232.7.182:5000/classify", json=query)
    print(res.json())
