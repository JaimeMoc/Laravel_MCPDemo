<?php

namespace App\Mcp\Tools;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use App\Models\Tarea;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Attributes\Description;
use Laravel\Mcp\Server\Tool;

#[Description('Crea una nueva tarea registrando nombre, descripción, responsable y status (por defecto pendiente).')]
class CrearTarea extends Tool
{
    /**
     * Handle the tool request.
     */
    public function handle(Request $request): Response
    {
        $validated = $request->validate([
            'nombre' => 'required|string|max:255',
            'descripcion' => 'nullable|string',
            'responsable' => 'required|string|max:255',
            'status' => 'nullable|string|in:pendiente,en_progreso,completada',
        ]);

        $tarea = Tarea::create([
            'nombre' => $validated['nombre'],
            'descripcion' => $validated['descripcion'] ?? null,
            'responsable' => $validated['responsable'],
            'status' => $validated['status'] ?? 'pendiente',
        ]);

        return Response::text(json_encode([
            'message' => 'Tarea creada exitosamente.',
            'tarea' => $tarea,
        ], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    }

    /**
     * Get the tool's input schema.
     *
     * @return array<string, JsonSchema>
     */
    public function schema(JsonSchema $schema): array
    {
        return [
            'nombre' => $schema->string()->description('Nombre de la tarea')->max(255),
            'descripcion' => $schema->string()->description('Descripción de la tarea')->nullable(),
            'responsable' => $schema->string()->description('Responsable de la tarea')->max(255),
            'status' => $schema->string()->description('Estado de la tarea (pendiente, en_progreso, completada)')->default('pendiente')->nullable(),
        ];
    }
}
