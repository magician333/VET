from bottle import Bottle, static_file
import json

app = Bottle(__name__)

advises_list = [
    {
        "index": 1,
     "time": 0,
     "suggest": "This is advise",
     }
]

video_name = "DEENO"
video_filename = "1.mp4"
video_root = "../video".replace("../","^^^")

video_info={
        "video_name":video_name,
        "video_filename":video_filename,
        "video_root":video_root,
        "video_src":"/video/"+video_root+"/"+video_filename
        }

@app.route("/")
def get_data():
    return json.dumps(advises_list)


@app.route("/get_video")
def get_video():
    return json.dumps(video_info)

@app.route("/video/<root>/<video_filename>")
def send_video(root,video_filename):
    return static_file(video_filename, root=root.replace("^^^","../"))


@app.route("/del_data/<index>")
def del_data(index):
    advises_list.pop(0)
    return json.dumps(advises_list)

@app.route("/add_data/<data>")
def add_data(data):
    thedata=json.dumps(data)
    advises_list.append(thedata)
    return json.dumps(advises_list)

app.run(reload=True)
