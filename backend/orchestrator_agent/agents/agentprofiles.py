import yaml

class AgentProfile:
    def __init__(self, agentprofilename: str):
        super().__init__()
        if not agentprofilename:
            raise ValueError("Agent profile name must be provided")
        if not isinstance(agentprofilename, str):
            raise TypeError("Agent profile name must be a string")
        
        config_file_path = 'orchestrator_agent/agents/agentprofiles.yml'
        with open(config_file_path, 'r', encoding='utf-8') as config_file:
            config_data = yaml.safe_load(config_file)
        
        # Find the profile in the agent_profile list
        template_config = None

        for profile in config_data.get('agent_profiles', []):
            if profile.get('agent_name') == agentprofilename:
                template_config = profile
                break

        if not template_config:
            raise ValueError(f"Agent profile '{agentprofilename}' not found in configuration yaml file.")
        
        self.name: str = template_config.get('agent_name')
        
        description_file_path = template_config.get('description_filepath')
        if description_file_path:
            with open(description_file_path, 'r', encoding='utf-8') as file:
                description_str = file.read()
        else:
            description_str = template_config.get('description', '')
        self.description: str = description_str

        instruction_file_path = template_config.get('instructions_filepath')
        if instruction_file_path:
            with open(instruction_file_path, 'r', encoding='utf-8') as file:
                instruction_str = file.read()
        else:
            instructions_str = template_config.get('instruction', '')
        self.instruction: str = instruction_str

        self.model_id: str = template_config.get('model_id')




