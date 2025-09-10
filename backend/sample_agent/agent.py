from google.adk.agents import Agent, LlmAgent
from .agents.agentprofiles import AgentProfile

trivia_agent_profile = AgentProfile(agent_name="trivia_agent")
trivia_agent = LlmAgent(
    name=trivia_agent_profile.name,
    model=trivia_agent_profile.model_id,
    description=trivia_agent_profile.description,
    instruction=trivia_agent_profile.instruction,
)

math_agent_profile = AgentProfile(agent_name="math_agent")
math_agent = LlmAgent(
    name=math_agent_profile.name,
    model=math_agent_profile.model_id,
    description=math_agent_profile.description,
    instruction=math_agent_profile.instruction,
)

science_agent_profile = AgentProfile(agent_name="science_agent")
science_agent = LlmAgent(
    name=science_agent_profile.name,
    model=science_agent_profile.model_id,
    description=science_agent_profile.description,
    instruction=science_agent_profile.instruction,
)

root_agent_profile = AgentProfile(agent_name="root_agent")
root_agent = Agent(
    name=root_agent_profile.name,
    model=root_agent_profile.model_id,
    description=root_agent_profile.description,
    instruction=root_agent_profile.instruction,
    sub_agents=[
        trivia_agent,
        math_agent,
        science_agent,
    ],
)