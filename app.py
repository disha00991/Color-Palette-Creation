# Importing essential libraries
from flask import Flask, send_file, request
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

"""
@app.route('/get_color_palette', methods=['POST','GET'])
def color_palette():
    ic(request.method)
    ic(request.form)

    if request.method == 'POST' or request.method == 'GET':
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
    return 'Get Color Palette!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# curl command
#>curl -X POST -d "is_url=true" -d "url=https://d21zeai4l2a92w.cloudfront.net/wp-content/uploads/2020/01/ColorChangingFlowers.jpg"
#  http://192.168.0.16:5000/get_color_palette --output palet.png