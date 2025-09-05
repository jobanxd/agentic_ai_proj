from google.adk.agents import Agent, LlmAgent
from .agents.agentprofiles import AgentProfile

trivia_agent_profile = AgentProfile(agentprofilename="trivia_agent")
trivia_agent = LlmAgent(
    name=trivia_agent_profile.name,
    model=trivia_agent_profile.model_id,
    description=trivia_agent_profile.description,
    instruction=trivia_agent_profile.instruction,
)

root_agent_profile = AgentProfile(agentprofilename="root_agent")
root_agent = Agent(
    name=root_agent_profile.name,
    model=root_agent_profile.model_id,
    description=root_agent_profile.description,
    instruction=root_agent_profile.instruction,
    sub_agents=[
        trivia_agent,
    ],
)