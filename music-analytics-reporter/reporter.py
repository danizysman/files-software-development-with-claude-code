#!/usr/bin/env python3
"""
Music Analytics Reporter - CLI tool for querying artist data from the Chinook database.

Usage:
    python reporter.py --artist "AC/DC" --format json --output report.json
    python reporter.py --artist "Aerosmith" --format csv --output report.csv
"""

import argparse
import sqlite3
import json
import csv
import sys
from pathlib import Path


def get_artist_data(db_path: str, artist_name: str) -> dict:
    """Query the Chinook database for an artist's albums and tracks."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Find artist
    cursor.execute(
        "SELECT ArtistId, Name FROM Artist WHERE Name LIKE ?",
        (f"%{artist_name}%",)
    )
    artist = cursor.fetchone()
    
    if not artist:
        conn.close()
        return None
    
    artist_id = artist["ArtistId"]
    artist_name = artist["Name"]
    
    # Get albums with track counts
    cursor.execute("""
        SELECT 
            a.AlbumId,
            a.Title,
            COUNT(t.TrackId) as track_count,
            SUM(t.Milliseconds) / 1000 as total_seconds
        FROM Album a
        LEFT JOIN Track t ON a.AlbumId = t.AlbumId
        WHERE a.ArtistId = ?
        GROUP BY a.AlbumId, a.Title
        ORDER BY a.Title
    """, (artist_id,))
    
    albums = []
    for row in cursor.fetchall():
        albums.append({
            "album_id": row["AlbumId"],
            "title": row["Title"],
            "track_count": row["track_count"],
            "total_seconds": row["total_seconds"] or 0
        })
    
    conn.close()
    
    return {
        "artist_id": artist_id,
        "artist_name": artist_name,
        "album_count": len(albums),
        "albums": albums
    }


def write_json(data: dict, output_path: str) -> None:
    """Write data to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_csv(data: dict, output_path: str) -> None:
    """Write data to a CSV file."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["artist_name", "album_title", "track_count", "total_seconds"])
        
        for album in data["albums"]:
            writer.writerow([
                data["artist_name"],
                album["title"],
                album["track_count"],
                album["total_seconds"]
            ])


def main():
    parser = argparse.ArgumentParser(
        description="Query artist data from the Chinook database and export to file."
    )
    parser.add_argument(
        "--artist",
        required=True,
        help="Artist name to search for (partial match supported)"
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        default="json",
        help="Output format (default: json)"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output file path"
    )
    parser.add_argument(
        "--db",
        default="chinook.db",
        help="Path to Chinook database (default: chinook.db)"
    )
    
    args = parser.parse_args()
    
    # Check database exists
    if not Path(args.db).exists():
        print(f"Error: Database not found at {args.db}", file=sys.stderr)
        sys.exit(1)
    
    # Query data
    data = get_artist_data(args.db, args.artist)
    
    if data is None:
        print(f"Error: No artist found matching '{args.artist}'", file=sys.stderr)
        sys.exit(1)
    
    # Write output
    if args.format == "json":
        write_json(data, args.output)
    else:
        write_csv(data, args.output)
    
    print(f"Report written to {args.output}")
    print(f"Found {data['album_count']} albums for {data['artist_name']}")
    sys.exit(0)


if __name__ == "__main__":
    main()
