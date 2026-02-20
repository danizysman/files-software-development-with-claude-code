import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_artist_albums_returns_artist_and_albums(client):
    response = client.get("/artists/1/albums")

    assert response.status_code == 200
    data = response.get_json()
    assert data["artist_id"] == 1
    assert data["artist_name"] == "AC/DC"
    assert len(data["albums"]) == 2
    titles = {album["Title"] for album in data["albums"]}
    assert titles == {"For Those About To Rock We Salute You", "Let There Be Rock"}


def test_get_artist_albums_response_shape(client):
    response = client.get("/artists/1/albums")

    assert response.status_code == 200
    data = response.get_json()
    assert set(data.keys()) == {"artist_id", "artist_name", "albums"}
    for album in data["albums"]:
        assert set(album.keys()) == {"AlbumId", "Title"}
        assert isinstance(album["AlbumId"], int)
        assert isinstance(album["Title"], str)


def test_get_artist_not_found(client):
    response = client.get("/artists/999999/albums")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Artist not found"}


def test_get_artist_with_no_albums(client):
    # Artist 25 (Milton Nascimento & Bebeto) exists but has no albums
    response = client.get("/artists/25/albums")

    assert response.status_code == 404
    assert response.get_json() == {"error": "No albums found for this artist"}
