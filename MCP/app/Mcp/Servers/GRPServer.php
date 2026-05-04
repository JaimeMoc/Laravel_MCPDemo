<?php

namespace App\Mcp\Servers;

use App\Mcp\Tools\CrearTarea;
use App\Mcp\Tools\ListarTareas;
use App\Mcp\Tools\BuscarTareaPorNombre;
use Laravel\Mcp\Server;
use Laravel\Mcp\Server\Attributes\Instructions;
use Laravel\Mcp\Server\Attributes\Name;
use Laravel\Mcp\Server\Attributes\Version;

#[Name('G R P Server')]
#[Version('1.0.0')]
#[Instructions('Instructions describing how to use the server and its features.')]
class GRPServer extends Server
{
    protected array $tools = [
        CrearTarea::class,
    ];

    protected array $resources = [
        //
    ];

    protected array $prompts = [
        //
    ];
}
