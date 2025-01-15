from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()


google_tool = SerperDevTool()

@CrewBase
class AgenticCrew():
	"""AgenticCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
 
	def __init__(self, document_tool):
	
		self.document_tool = document_tool

	@agent
	def retriever_agent(self) -> Agent:
		return Agent(
			config=self.agents_config["retriever_agent"],
   			tools=[self.document_tool, google_tool], 
			verbose = True
		)

	@agent
	def update_retriever_agent(self) -> Agent:
		return Agent(
			config=self.agents_config["update_retriever_agent"],
			tools=[self.document_tool, google_tool], 
			verbose = True
		)
        
	@agent
	def response_agent(self) -> Agent:
		return Agent(
			config=self.agents_config["response_agent"],
			tools=[self.document_tool, google_tool], 
			verbose = True
		)
        
	@agent
	def update_response_agent(self) -> Agent:
		return Agent(
			config=self.agents_config["update_response_agent"],
			tools=[self.document_tool, google_tool], 
			verbose = True
		)
        
	@task
	def retriever_agent_task(self) -> Task:
		return Task(
			config=self.tasks_config["retriever_agent_task"],
		)
        
	@task
	def update_retriever_agent_task(self) -> Task:
		return Task(
			config=self.tasks_config["update_retriever_agent_task"],
		)
        
	@task
	def response_agent_task(self) -> Task:
		return Task(
			config=self.tasks_config["response_agent_task"],
		)
        
	@task
	def update_response_agent_task(self) -> Task:
		return Task(
			config=self.tasks_config["update_response_agent_task"],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AgenticCrew crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
