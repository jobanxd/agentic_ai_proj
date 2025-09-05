from google.adk.agents import Agent, LlmAgent
from .agents.agentprofiles import AgentProfile


root_agent_profile = AgentProfile(agentprofilename="root_agent")
root_agent = Agent(
    name=root_agent_profile.name,
    model=root_agent_profile.model_id,
    description=root_agent_profile.description,
    instruction=root_agent_profile.instruction,
)