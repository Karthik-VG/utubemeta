from videolist import videolist
from videotags import videotags
from flask_cors import cross_origin
import pandas as pd

def home(word):
    temp=word.split("_")
    keyword=" ".join(temp)
    vlist_temp = videolist(keyword)
    links, ynames = vlist_temp.search()
    tags_temp = videotags()
    bulk_out = []

    for i in links:
        bulk_out.append(tags_temp.videotags(i))
    print(bulk_out)
    print(len(bulk_out))
    print("/n"*10)
    for count in range(len(bulk_out)):
        bulk_out[count]["channel_name"] = ynames[count]
    print(bulk_out)
    df_temp = pd.DataFrame(bulk_out)
    df_temp = df_temp[["title", "views", "tags", "channel_name", "description"]]
    df_temp.to_html("templates/homepage.html")

home("chennai_flood")