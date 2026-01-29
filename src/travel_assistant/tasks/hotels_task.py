from crewai.task import Task
from travel_assistant.agents.hotels_agent import hotels_agent

hotels_task = Task(
    name="Hotels Task",
    description=
        "Suggest 3 to 5 hotels in {destination}. "
        "For each hotel include:\n"
        "- Hotel name\n"
        "- Estimated price per night (USD)\n"
        "- Area or neighborhood\n"
        "- Short reason why it’s recommended\n\n"
        "Assume the data is realistic but does not need to be real.",
    agent=hotels_agent,
    input_schema={
        "destination": "The city or country to which the user wants hotel recommendations.",
    },
    output_schema={
        "hotels": "A well-structured list of hotel recommendations with prices and descriptions."
    },
    verbose=True,
)