# Importing essential libraries
from flask import Flask, request, make_response, jsonify
# from flask_cors import CORS, cross_origin
from color_palette_creation import get_palette_plot
from PIL import Image
from io import BytesIO
import requests
from icecream import ic

app = Flask(__name__)

"""
@todo
input other algorithm for clustering @todo
send rgb color values for use by user @todo
home end point here -> deployed frontend link
image can be uploaded from frontend too
"""
@app.route('/get_color_palette', methods=['POST','GET', 'OPTIONS'])
def color_palette():
    is_url = request.args['is_url']
    algo = request.args['algo']
    url = request.args['url']
    n_colors = request.args['n_colors']
    print("partt")
    if request.method == "OPTIONS": # CORS preflight
        print('preflight')
        return _build_cors_prelight_response()
    if request.method == 'POST' or request.method == 'GET':
        img = ''
        if (is_url=='true' and url):
            img = Image.open(BytesIO(requests.get(url).content))
        # else:
        #     img = Image.open(request.files['file'])

    return _corsify_actual_response(jsonify(get_palette_plot(img, algo, int(n_colors))))

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/')
def home_endpoint():
    return "<h1>This is the Flask app for Color Palette Creation Project hosted at <a href='https://disha00991.github.io/webume/#/projects/color-palette'>here</a></h1>"

if __name__ == '__main__':
    app.run()


# curl command
#>curl -X POST -d "is_url=true" -d "url=https://d21zeai4l2a92w.cloudfront.net/wp-content/uploads/2020/01/ColorChangingFlowers.jpg" http://127.0.0.1:5000/get_color_palette --output palet.png