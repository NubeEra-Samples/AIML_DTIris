from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "<b>Welcome Python From Flask with Docker</b>"

if __name__=="__main__":
    app.run(debug=True)
    #app.run(debug=True,host="0.0.0.0",port=5000)