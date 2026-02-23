---
name: generate-stats
description: Generate statistics functions for music data
---

# Generate Statistics Command

When asked to generate statistics, create a function that:

1. Accepts a list of music data (artists, albums, or tracks)
2. Calculates relevant metrics (counts, averages, totals)
3. Returns a dictionary with labeled results
4. Includes proper error handling for empty lists
5. Uses type hints and docstrings

Example output format:
```python
def calculate_artist_stats(artists: list[dict]) -> dict:
    """Calculate statistics for a list of artists."""
    if not artists:
        return {'error': 'No artists provided'}
    ...
```
