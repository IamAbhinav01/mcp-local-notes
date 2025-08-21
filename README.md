# MCP Server

## Installation Steps

1. Add the following configuration to your `.mcp/config.json`:

```json
{
  "mcpServers": {
    "localmcpserver": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/IamAbhinav01/mcp-local-notes.git",
        "mcp-server"
      ]
    }
  }
}
```

2. The server will be available as 'localmcpserver' in your MCP configuration.

## Usage

Once configured, you can start using the MCP server for local notes management.
