from flask import Flask, request,render_template,Response
from apathy_perception import perception

app = Flask(__name__)

@app.route('/apathy')
def apathy():
    return Response(perception(),mimetype='multipart/x-mixed-replace;boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)