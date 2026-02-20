# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
```

The API runs on port 5000 with debug mode enabled by default.

## Architecture

This is a simple Flask REST API for task management with the following structure:

- **app.py**: Application entry point - registers blueprints and middleware
- **routes.py**: API endpoint definitions using Flask blueprints
- **models.py**: Data models and in-memory storage functions
- **middleware.py**: Request logging middleware and decorators
- **config.py**: Configuration classes for different environments

### Key Architectural Patterns

**Storage**: Uses in-memory storage (`_tasks` list in models.py), not a database. Data is lost on restart.

**Sessions**: The project is configured to use **filesystem-based sessions** (see `config.py`), not JWT or token-based authentication. When adding authentication or session features, extend the existing filesystem session pattern defined in `Config.SESSION_TYPE` and `Config.SESSION_FILE_DIR`.

**Middleware**: Custom middleware is applied via class-based wrappers (see `RequestLogger` in middleware.py) that register Flask hooks using `before_request` and `after_request`.

**Configuration**: Uses class-based config pattern with environment-specific subclasses (DevelopmentConfig, ProductionConfig). The active config is set at module level in config.py.

## API Endpoints

- `GET /api/tasks` - List all tasks
- `POST /api/tasks` - Create a task (requires JSON body with 'title', optional 'description')
- `GET /api/tasks/<id>` - Get specific task by ID
