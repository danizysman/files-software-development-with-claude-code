# Claude Code SQLite MCP Server Configuration

Enable SQLite database access in Claude Code using the Model Context Protocol (MCP).

## Setup

### Option 1: Project-Level (This Project Only)

1. Create `.claude/mcp.json` in your project root with your database path:

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "$PWD/path/to/your/database.db"]
    }
  }
}
```

Replace `path/to/your/database.db` with your actual database file path.

2. Restart Claude Code to load the configuration.

### Option 2: Global (All Projects)

Run this command once in your terminal:

```bash
claude mcp add-json sqlite '{"command":"uvx","args":["mcp-server-sqlite","--db-path","path/to/your/database.db"]}'
```

This adds SQLite MCP server to `~/.claude/mcp.json` automatically. You can now use SQLite in all your Claude Code projects.

## What You Can Do

Once configured, Claude Code can:
- List tables in your database
- Describe table schemas
- Run read queries (SELECT statements)
- Execute bash commands with sqlite3

## Example

After setup, you can ask Claude Code:
- "Show me the structure of the users table"
- "Run a SELECT query to get all records from the products table"
- "What tables are in this database?"
