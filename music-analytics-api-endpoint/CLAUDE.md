# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
pip install flask
```

The app requires `chinook.db` (SQLite) to be present in the project root. This is the [Chinook sample music database](https://github.com/lerocha/chinook-database).

## Running the App

```bash
python3 app.py
```

Starts Flask dev server at `http://localhost:5000` with debug mode enabled.

## Architecture

Single-file Flask REST API (`app.py`) backed by SQLite (`chinook.db`).

- `get_db()` — opens a SQLite connection with `row_factory = sqlite3.Row` (enables dict-style row access)
- Routes query the database directly and return JSON; connections are closed in a `finally` block

**Current endpoint:**
- `GET /artists/<artist_id>/albums` — returns albums for an artist as JSON array (returns empty array if artist not found or has no albums)

**Exercise goal:** Add Pydantic validation and proper 404 error handling.

**Relevant Chinook tables:** `artists` (ArtistId, Name), `albums` (AlbumId, Title, ArtistId)
