from bottle import Bottle, static_file
import json
app = Bottle(__name__)

advises_list = [
    {"index": 1,
     "time": 0,
     "suggest": "This is advise",
     }
]


@app.route("/")
def get_data():
    return json.dumps(advises_list)


@app.route("/get_video")
def get_video():
    return static_file("1.mp4", root="../video")


@app.route("/del_data/<index>")
def del_data(index):
    advises_list.pop(0)
    return json.dumps(advises_list)


app.run(host="127.0.0.1", reload=True)
