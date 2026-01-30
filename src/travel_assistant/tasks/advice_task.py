from crewai import Task
from travel_assistant.agents.advice_agent import advice_agent

advice_task = Task(
    description=(
        "Provide practical and detailed travel advice for a trip to {destination}.\n\n"
        "Include tips on:\n"
        "- Best time to visit\n"
        "- Must-see attractions and recommended activities\n"
        "- Local customs and etiquette\n"
        "- Transportation and getting around\n"
        "- Budgeting tips\n"
        "- Safety considerations\n"
        "- Packing essentials\n"
        "- Common mistakes to avoid\n\n"
        "Tailor the advice to the destination and, when available, to user preferences. "
        "Keep the recommendations realistic, actionable, and easy to follow."
    ),
    agent=advice_agent,
    input_schema={
        "destination": "The city or country to which the user wants advice on."
    },
    output_schema={
        "travel_advice": "A comprehensive set of travel tips and recommendations customized for the user."
    },
    verbose=True,
)
