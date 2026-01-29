#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from travel_assistant.crew import TravelAssistant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# ----------------------------
# Default CrewAI methods (keep for future use)
# ----------------------------

def run():
    """Run the crew."""
    inputs = {
        'topic': 'Travel Assistant',
        'current_year': str(datetime.now().year)
    }

    try:
        TravelAssistant().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """Train the crew for a given number of iterations."""
    inputs = {
        "topic": "Travel Assistant",
        'current_year': str(datetime.now().year)
    }
    try:
        TravelAssistant().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """Replay the crew execution from a specific task."""
    try:
        TravelAssistant().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """Test the crew execution and return the results."""
    inputs = {
        "topic": "Travel Assistant",
        "current_year": str(datetime.now().year)
    }

    try:
        TravelAssistant().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """Run the crew with trigger payload."""
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = TravelAssistant().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")


# ----------------------------
# Quick test for Flight Task
# ----------------------------

if __name__ == "__main__":
    crew = TravelAssistant()

    print("==== Travel Assistant Quick Test ====")
    destination = input("Enter your travel destination: ")

    task_input = {
        "destination": destination
    }

    output = crew.run_task("flight_task", task_input)

    print("\nFlight Task Output:")
    for flight in output.get("flights", output):  # handles list or dict return
        print(f"- {flight}")
