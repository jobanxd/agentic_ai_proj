import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from hrmanager_agent.agent import root_agent

from google.genai import types as genai_types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory import InMemoryMemoryService

# Init services for Runner
session_svc = InMemorySessionService()
artifact_svc = InMemoryArtifactService()
memory_svc = InMemoryMemoryService()

logger = logging.getLogger(__name__)
router = APIRouter()

class UnifiedAgentRequest(BaseModel):
    input_query: str

class UnifiedAgentResponse(BaseModel):
    response: str

@router.post("/generate", response_model=UnifiedAgentResponse)
async def generate_respones(request: UnifiedAgentRequest):
    try:
        session_id = "1234"
        user_id = "1234"

        session = await session_svc.create_session(
            app_name="Unified Agents",
            user_id=user_id,
            session_id=session_id,
        )

        logger.info("Session: %s", session)

        runner = Runner(
            agent=root_agent,
            app_name="Unified Agents",
            session_service=session_svc,
            memory_service=memory_svc,
            artifact_service=artifact_svc,
        )

        user_content = genai_types.Content(
            role="user",
            parts=[genai_types.Part(text=request.input_query)]
        )

        events = runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=user_content,
        )

        response_parts=[]

        async for event in events:
            if hasattr(event, 'content') and event.content:
                if hasattr(event.content, 'parts'):
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            response_parts.append(part.text)
        
        response_message = "".join(response_parts).strip()
        
        return UnifiedAgentResponse(response=response_message)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    