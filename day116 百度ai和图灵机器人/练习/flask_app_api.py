from flask import Flask, request, render_template,send_file

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index1.html")


@app.route("/get_audio/<audio_name>")
def get_audio(audio_name):
    return send_file(audio_name)


if __name__ == '__main__':
    app.run("0.0.0.0", 9527, debug=True)