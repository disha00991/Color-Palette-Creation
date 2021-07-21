# Importing essential libraries
from flask import Flask, send_file, request
from flask_cors import CORS
from color_palette_creation import get_palette_plot
from PIL import Image
from io import BytesIO
import requests
from icecream import ic

app = Flask(__name__)
CORS(app)

"""
@todo
input other algorithm for clustering @todo
send rgb color values for use by user @todo
home end point here -> deployed frontend link
image can be uploaded from frontend too
"""
@app.route('/get_color_palette', methods=['POST','GET'])
def color_palette():
    ic(request.method)
    ic(request.form)
    print("partt")
    if request.method == 'POST' or request.method == 'GET':
        print("part2")
        img = ''
        if (request.form['is_url']=='true'):
            img = Image.open(BytesIO(requests.get(request.form['url']).content))
        else:
            img = Image.open(request.files['file'])
        bytes_obj = get_palette_plot(img)
       
    return send_file(bytes_obj,
                     download_name='palette.png',
                     mimetype='image/png')

@app.route('/')
def home_endpoint():
    url = 'https://abc.in'
    return "<h1>This is the Flask app for Color Palette Creation Project hosted at <a href='https://disha00991.github.io/webume/#/projects/color-palette'>here</a></h1>"

if __name__ == '__main__':
    print('whatt?')
    app.run(host='0.0.0.0', port=8080)


# curl command
#>curl -X POST -d "is_url=true" -d "url=https://d21zeai4l2a92w.cloudfront.net/wp-content/uploads/2020/01/ColorChangingFlowers.jpg" http://192.168.0.16:5000/get_color_palette --output palet.png