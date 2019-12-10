from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    title = request.args.get('title', type=str)
    data = requests.get(
        "http://api.deezer.com/search?q={}".format(title)).json()
    track = data["data"][0]
    album = track["album"]
    title = track["title"]
    artist = track["artist"]["name"]
    albumName = album["title"]

    if "cover_xl" in album:
        coverAlbum = album["cover_xl"]
    else:
        coverAlbum = album["cover_big"]

    return jsonify({
        "title": title,
        "artists": [artist],
        "albumName": albumName,
        "albumCover": coverAlbum
    })


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
