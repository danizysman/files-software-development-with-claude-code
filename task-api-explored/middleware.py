"""Request Logging Middleware (exercise variant)."""
import logging
from datetime import datetime

def setup_logging(app):
    """Configure request logging for the application."""

    @app.before_request
    def log_request():
        app.logger.info(f"[{datetime.utcnow().isoformat()}] Request started")

    @app.after_request
    def log_response(response):
        app.logger.info(f"[{datetime.utcnow().isoformat()}] Response: {response.status}")
        return response

    # Configure logging format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
