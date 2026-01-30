from crewai import Task
from travel_assistant.agents.tours_agent import tours_agent

tours_task = Task(
    description=
        "Create a {days}-day travel itinerary for {destination}. "
        "Each day should include:\n"
        "- Morning activity\n"
        "- Afternoon activity\n"
        "- Evening activity\n"
        "- Estimated price (USD)\n"
        "- Short explanation\n\n"
        "The plan should feel realistic and balanced.",
    agent=tours_agent,
    input_schema={
        "destination": "The city or country to which the user wants tour recommendations.",
        "days": "The number of days for the itinerary.",
    },
    output_schema={
        "tours": "A structured day-by-day travel plan with prices and descriptions."
    },
    verbose=True,
)