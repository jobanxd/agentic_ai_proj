from pydantic import BaseModel

class UnifiedAgentRequest(BaseModel):
    agent_name: str
    session_id: str
    user_id: str
    input_query:str

class UnifiedAgentResponse(BaseModel):
    response: str

