from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class FlightToolInput(BaseModel):
    """Input schema for FlightToolInput."""
    destination: str = Field(..., description="Destination city or country.")

class FlightSearchTool(BaseTool):
    name: str = "Flight Search Tool"
    description: str = (
        "Returns a list of dummy flights for a given destination."
    )
    args_schema: Type[BaseModel] = FlightToolInput

    def _run(self, destination: str) -> str:
        flights = [
        f"Flight A to {destination}",
        f"Flight B to {destination}",
        f"Flight C to {destination}",
    ]
        return "\n".join(flights)
    

"""
What input does this tool expect?

What does _run() do?

Why does the agent need name and description?

The tool expects an input of type FlightToolInput, which contains a single field 'destination' representing the destination city or country.
The _run() method generates a list of dummy flight options to the specified destination and returns them as a formatted string.
The agent needs the name and description to identify the tool and understand its purpose, which helps in selecting the appropriate tool for a given task.
"""