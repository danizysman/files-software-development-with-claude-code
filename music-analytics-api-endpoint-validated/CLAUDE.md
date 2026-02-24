# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
pip install flask pydantic
python app.py
```

Requires `chinook.db` (SQLite) in the working directory. The server starts on `http://127.0.0.1:5000` with debug mode enabled.

## Architecture

Single-file Flask API (`app.py`) with one endpoint:

- **`GET /artists/<artist_id>/albums`** — returns albums for a given artist

**Request flow:** Flask route → SQLite queries (artists, albums tables) → Pydantic validation → JSON response

**Pydantic models:**
- `Album` — `AlbumId: int`, `Title: str`
- `ArtistAlbumsResponse` — `artist_id`, `artist_name`, `albums: list[Album]`

**Database:** `get_db()` opens a new SQLite connection per request using `sqlite3.Row` as the row factory (enables dict-like column access). The connection is always closed in a `finally` block.
