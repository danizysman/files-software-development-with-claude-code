# Music Analytics Reporter

A CLI tool for generating reports from the Chinook music database.

## Project Structure

- `reporter.py` - Main CLI tool
- `chinook.db` - SQLite database with music catalog data

## Usage

```bash
python reporter.py --artist "AC/DC" --format json --output report.json
python reporter.py --artist "Aerosmith" --format csv --output report.csv
```

## Database Schema

The Chinook database contains:
- `Artist` - Artist information (ArtistId, Name)
- `Album` - Albums linked to artists (AlbumId, Title, ArtistId)
- `Track` - Tracks on albums (TrackId, Name, AlbumId, Milliseconds)

## Testing

Use pytest for testing:
```bash
pytest test_reporter.py -v
```
