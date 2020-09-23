import flask
import os

app = flask.Flask(__name__)

artists = ["Ariana Grande", "Taylor Swift", "Katy Perry", "Camila Cabello", "Blackpink"]
artistsPhoto = ["/static/ariana.jpg", "/static/taylor.jpg", "/static/katy.jpg", "/static/camila.jpg", "/static/blackpink.jpg"]

@app.route('/')

def index():
    #return "Hello World!"
    
    return flask.render_template(
        "index.html",
        length = len(artists),
        artists = artists,
        artistsPhoto = artistsPhoto,
        length_photo = len(artistsPhoto)
        )
    
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP" "0.0.0.0")
)
