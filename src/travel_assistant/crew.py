from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import List
from travel_assistant.agents.flight_agent import flight_agent
from travel_assistant.tasks.flight_task import flight_task
from travel_assistant.agents.hotels_agent import hotels_agent
from travel_assistant.tasks.hotels_task import hotels_task
from travel_assistant.agents.tours_agent import tours_agent
from travel_assistant.tasks.tours_task import tours_task
from travel_assistant.agents.advice_agent import advice_agent
from travel_assistant.tasks.advice_task import advice_task


@CrewBase
class TravelAssistant:
    """Travel Assistant crew"""

    agents: List[Agent]
    tasks: List[Task]

  
    # @agent
    # def reporting_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['reporting_analyst'], # type: ignore[index]
    #         verbose=True
    #     )

    @agent
    def flight_agent(self) -> Agent:
        return flight_agent

    """
    - Use config=... only for YAML-based agents/tasks

    - Use direct references (flight_agent) for Python-defined ones 
    """
    @agent
    def hotels_agent(self) -> Agent:
        return hotels_agent
    
    @agent
    def tours_agent(self) -> Agent:
        return tours_agent
    
    @agent
    def advice_agent(self) -> Agent:
        return advice_agent
    
    
    @task
    def flight_task(self) -> Task:
        return flight_task
    
    @task
    def hotels_task(self) -> Task:
        return hotels_task

    @task
    def tours_task(self) -> Task:
        return tours_task
    
    @task
    def advice_task(self) -> Task:
        return advice_task
    

    @crew
    def crew(self) -> Crew:
        """Creates the TravelAssistant crew"""
      
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
