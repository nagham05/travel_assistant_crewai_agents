from crewai import Task
from agents.flight_agent import flight_agent

flight_task = Task(
    name="Flight Task",
    description="Get available flights for the user's requested destination.",
    agent=flight_agent,
    input_schema={
        "destination": "The city or country to which the user wants to find flights."
    },
    output_schema={
        "flights": "A list of available flights to the specified destination."
    },
    verbose=True,
)