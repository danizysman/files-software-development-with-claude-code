"""Application Configuration (exercise variant; same SESSION_TYPE as video for MCQ)."""
import os

class Config:
    """Flask configuration settings."""

    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')

    # Session configuration - uses filesystem storage
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = '/tmp/flask_sessions'
    SESSION_PERMANENT = False

    # API settings
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
