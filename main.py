from flask import Flask, render_template, request, jsonify
from videolist import videolist
from videotags import videotags
from flask_cors import cross_origin
import pandas as pd

app = Flask(__name__)



@app.route("/")
@cross_origin()
def base():
    return "Welcome to eleinsider"

@app.route("/<word>")
@cross_origin()
def home(word):
    temp = word.split("_")
    keyword = " ".join(temp)
    vlist_temp = videolist(keyword)
    links, ynames = vlist_temp.search()
    tags_temp = videotags()
    bulk_out = []

    for i in links:
        bulk_out.append(tags_temp.videotags(i))

    for count in range(len(bulk_out)):
        bulk_out[count]["channel_name"] = ynames[count]

    df_temp = pd.DataFrame(bulk_out)
    df_temp = df_temp[["title", "views","channel_name", "tags", "description"]]


    return df_temp.to_html()


@app.route("/tags", methods=["GET", "POST"])
@cross_origin()
def search():
    if request.method == 'POST':
        req = request.get_json()
        keyword = req["key"]
        vlist_temp = videolist(keyword)
        links, ynames = vlist_temp.search()
        tags_temp = videotags()
        bulk_out = []

        for i in links:
            bulk_out.append(tags_temp.videotags(i))
        for count in range(len(bulk_out)):
            bulk_out[count]["channel_name"] = ynames[count]

        return {"meta": bulk_out}

    return "Please send the request with informations on body"


if __name__ == "__main__":
    app.run(debug=True)
