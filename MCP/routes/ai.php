<?php

use App\Mcp\Servers\GRPServer;
use Laravel\Mcp\Facades\Mcp;

// Exponer el servidor MCP por HTTP para Claude Desktop
Mcp::web('/mcp/grp', GRPServer::class);