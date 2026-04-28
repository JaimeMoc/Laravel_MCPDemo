from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class ToolParameter(BaseModel):
    """
    Defines a parameter for a tool.
    """

    name: str = Field(
        ...,
        description="Parameter name"
    )

    type: str = Field(
        ...,
        description="Parameter type"
    )

    required: bool = Field(
        default=True,
        description="Whether parameter is required"
    )

    description: Optional[str] = Field(
        default=None,
        description="Parameter description"
    )

class ToolSchema(BaseModel):
    """
    Defines a tool structure.
    """

    name: str = Field(
        ...,
        description="Tool name"
    )

    description: str = Field(
        ...,
        description="Tool description"
    )

    parameters: Dict[str, ToolParameter] = Field(
        default_factory=dict,
        description="Tool parameters"
    )

class ToolRequest(BaseModel):
    """
    Request sent to a tool.
    """

    tool_name: str = Field(
        ...,
        description="Tool to execute"
    )

    payload: Dict[str, Any] = Field(
        default_factory=dict,
        description="Tool input data"
    )

class ToolResponse(BaseModel):
    """
    Response returned by a tool.
    """

    success: bool = Field(
        ...,
        description="Execution status"
    )

    result: Optional[Any] = Field(
        default=None,
        description="Tool result"
    )

    error: Optional[str] = Field(
        default=None,
        description="Error message"
    )