from bottle import Bottle, static_file, request
import json

app = Bottle(__name__)

advises_list = [
    {
        "index": 1,
        "time": 0,
        "advise": "This is advise",
    },
    {
        "index": 2,
        "time": 12,
        "advise": "This is advise2",
    },
    {
        "index": 3,
        "time": 11,
        "advise": "This is advise3",
    }
]

video_name = "DEENO"
video_filename = "1.mp4"
video_root = "../video".replace("../", "^^^")

video_info = {
    "video_name": video_name,
    "video_filename": video_filename,
    "video_root": video_root,
    "video_src": "/video/"+video_root+"/"+video_filename
}


@app.route("/")
def get_data():
    return json.dumps(advises_list)


@app.route("/get_video")
def get_video():
    return json.dumps(video_info)


@app.route("/video/<root>/<video_filename>")
def send_video(root, video_filename):
    return static_file(video_filename, root=root.replace("^^^", "../"))


@app.route("/del_data", method="POST")
def del_data():
    del_index = eval(request.body.read().decode())["del_index"]
    print(del_index)
    advises_list.pop(del_index-1)
    return json.dumps(advises_list)


@app.route("/add_data", method="POST")
def add_data():
    thedata = json.dumps(eval(request.body.read().decode())["data"])
    advises_list.append(thedata)
    return json.dumps(advises_list)


app.run(reload=True)
