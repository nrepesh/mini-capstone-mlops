import imageio
from flask import Flask
from io import BytesIO
import base64
from pydantic import BaseModel
from flask_pydantic import validate
from tensorflow import keras
import numpy as np
from labels import labels
import sys

model = keras.models.load_model('model.h5')

app = Flask(__name__)

labels_names = []
for i in range(len(labels)):
    labels_names += [i]

reverse_mapping = dict(zip(labels_names, labels))


def mapper(value):
    return reverse_mapping[value]


class RequestBodyModel(BaseModel):
    id: int
    b64img: str


class ResponseModel(BaseModel):
    id: int
    label: str


def read_encoded_img(encoded):
    img = imageio.imread(BytesIO(base64.b64decode(encoded)), as_gray=False, pilmode="RGB")
    return img


@app.route('/classify', methods=["POST"])
@validate()
def classify(body: RequestBodyModel):
    image = read_encoded_img(body.b64img)
    image = np.resize(image, (32, 32, 3))
    image = image / 255.0
    prediction_image = np.array(image)
    prediction_image = np.expand_dims(image, axis=0)
    prediction = model.predict(prediction_image)
    print("num of predictions", len(prediction))
    value = np.argmax(prediction)
    name = mapper(value)

    return ResponseModel(
        id=body.id,
        label=name
    )


if __name__ == "__main__":
    if "serve" in sys.argv:
        app.run(debug=False, port=5000, host='0.0.0.0')
