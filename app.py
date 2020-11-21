import base64
import json
from io import BytesIO
import base64
from flask import Flask, jsonify, request, send_file
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from PIL import Image
from main import main

app = Flask(__name__)
api = Api(app)
CORS(app)

image_req_args = reqparse.RequestParser()
image_req_args.add_argument("image", type=str)

class Predict(Resource):
    
    def post(self):
        args = image_req_args.parse_args()
        base64Image = args['image'].split(',',1)[1]
        operation = BytesIO(base64.urlsafe_b64decode(base64Image))
        Image.open(operation).save('input.png')
        main('input.png')
        output_file = 'emotion-activity.png'
        img = Image.open(output_file, mode='r')
        imgBytes = BytesIO()
        img.save(imgBytes, format='PNG')
        encodedImage = base64.encodebytes(imgBytes.getvalue()).decode('ascii')
        return jsonify({
            'image': encodedImage
        })

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run()