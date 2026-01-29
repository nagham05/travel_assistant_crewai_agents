from crewai import Agent
from travel_assistant.tools.flight_tool import FlightSearchTool


flight_agent = Agent(
    role="Flight Search Specialist",
    goal="Find available flights to the user's requested destination",
    backstory=(
        "You are a reliable travel assistant focused only on retrieving "
        "flight options using the provided flight search tool. "
        "You never invent data."
    ),
    tools=[FlightSearchTool()],
    verbose=True,
)

