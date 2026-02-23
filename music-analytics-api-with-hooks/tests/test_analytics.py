"""Tests for analytics functions."""

import pytest
from analytics import calculate_album_stats


def test_calculate_album_stats_filters_by_track_count():
    """Albums with track_count <= min_tracks should be filtered out."""
    albums = [
        {'album_id': 1, 'title': 'Small Album', 'track_count': 3, 'popularity': 50},
        {'album_id': 2, 'title': 'Big Album', 'track_count': 10, 'popularity': 80},
    ]
    result = calculate_album_stats(albums, min_tracks=5)
    
    assert len(result) == 1
    assert result[0]['album_id'] == 2


def test_calculate_album_stats_applies_multiplier():
    """Popularity should be multiplied by the multiplier."""
    albums = [
        {'album_id': 1, 'title': 'Test Album', 'track_count': 10, 'popularity': 50},
    ]
    result = calculate_album_stats(albums, multiplier=2.0)
    
    assert result[0]['adjusted_popularity'] == 100.0


def test_calculate_album_stats_assigns_tier():
    """Albums should be assigned platinum or gold tier based on adjusted popularity."""
    albums = [
        {'album_id': 1, 'title': 'Popular', 'track_count': 10, 'popularity': 100},
        {'album_id': 2, 'title': 'Less Popular', 'track_count': 10, 'popularity': 50},
    ]
    result = calculate_album_stats(albums)
    
    platinum = next(a for a in result if a['album_id'] == 1)
    gold = next(a for a in result if a['album_id'] == 2)
    
    assert platinum['tier'] == 'platinum'
    assert gold['tier'] == 'gold'


def test_calculate_album_stats_returns_top_5():
    """Should return at most 5 albums."""
    albums = [
        {'album_id': i, 'title': f'Album {i}', 'track_count': 10, 'popularity': i * 10}
        for i in range(1, 10)
    ]
    result = calculate_album_stats(albums)
    
    assert len(result) == 5


def test_calculate_album_stats_empty_list():
    """Should handle empty album list."""
    result = calculate_album_stats([])
    assert result == []
