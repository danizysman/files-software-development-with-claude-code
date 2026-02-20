import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
DB_PATH = "chinook.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/artists/<int:artist_id>/albums")
def get_artist_albums(artist_id):
    conn = get_db()
    try:
        artist = conn.execute(
            "SELECT ArtistId, Name FROM artists WHERE ArtistId = ?", (artist_id,)
        ).fetchone()
        if artist is None:
            return jsonify({"error": "Artist not found"}), 404
        albums = conn.execute(
            "SELECT AlbumId, Title FROM albums WHERE ArtistId = ?", (artist_id,)
        ).fetchall()
    finally:
        conn.close()
    if not albums:
        return jsonify({"error": "No albums found for this artist"}), 404
    response = {
        "artist_id": artist["ArtistId"],
        "artist_name": artist["Name"],
        "albums": [{"AlbumId": row["AlbumId"], "Title": row["Title"]} for row in albums],
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)