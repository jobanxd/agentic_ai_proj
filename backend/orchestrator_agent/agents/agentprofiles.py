import yaml

class AgentProfile:
    def __init__(self, agent_name: str):
        if not agent_name:
            raise ValueError("Agent name is required!")

        # Load the YAML config    
        agent_profiles_filepath = 'orchestrator_agent/agents/agentprofiles.yml'
        
        with open(agent_profiles_filepath, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

        # Find the agent profile
        profile = None
        for profile in config['agent_profiles']:
            if profile['agent_name'] == agent_name:
                agent_profile = profile
                break

        if not agent_profile:
            raise ValueError(f"Agent '{agent_name}' not found")
        
        # Set properties directly from YAML
        self.name = agent_profile['agent_name']
        self.model_id = agent_profile['model_id']

        # Load description from file
        with open(agent_profile['description_filepath'], 'r', encoding='utf-8') as file:
            self.description = file.read()

        # Load instruction from file
        with open(agent_profile['instructions_filepath'], 'r', encoding='utf-8') as file:
            self.instruction = file.read()
            