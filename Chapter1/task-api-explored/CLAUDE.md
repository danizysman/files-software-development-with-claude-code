# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Application

```bash
python app.py
```

The Flask app runs in debug mode by default on http://localhost:5000.

## Architecture

This is a minimal Flask REST API for task management with no database persistence.

### Module Responsibilities

- **app.py**: Flask app entry point. Imports routes using `from routes import *` after app initialization to avoid circular imports.
- **config.py**: Configuration class loaded via `app.config.from_object(Config)`. Uses filesystem-based sessions (SESSION_TYPE = 'filesystem').
- **middleware.py**: Request/response logging setup via `@app.before_request` and `@app.after_request` decorators.
- **models.py**: `TaskStore` class provides in-memory task storage with no persistence between restarts.
- **routes.py**: API endpoints that use `session.get('user_id', 'anonymous')` for user identification.

### Key Design Patterns

- **Session-based user tracking**: Users are identified by `session['user_id']`, defaulting to 'anonymous' if not set.
- **In-memory storage**: All tasks are stored in `TaskStore._tasks` dictionary and lost on restart.
- **Circular import pattern**: Routes import `app` from app.py, while app.py imports routes after app initialization.

### API Endpoints

- `GET /tasks` - Returns tasks for current session user
- `POST /tasks` - Creates task (requires JSON with 'title', optional 'description')
- `DELETE /tasks/<task_id>` - Deletes task by ID

## Session Storage

Sessions are stored in `/tmp/flask_sessions` as configured in config.py. This directory must be writable.
