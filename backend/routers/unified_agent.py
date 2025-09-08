import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from hrmanager_agent.agent import root_agent as hrmanager_root_agent
from sample_agent.agent import root_agent as sample_root_agent

from google.genai import types as genai_types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory import InMemoryMemoryService

from models.unified_agent import (
    UnifiedAgentResponse,
    UnifiedAgentRequest
)

# Init services for Runner
session_svc = InMemorySessionService()
artifact_svc = InMemoryArtifactService()
memory_svc = InMemoryMemoryService()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/generate", response_model=UnifiedAgentResponse)
async def generate_respones(request: UnifiedAgentRequest):
    try:

        if request.agent_name == "sample_agent":
            final_agent = sample_root_agent
        elif request.agent_name == "hrmanager_agent":
            final_agent = hrmanager_root_agent

        session = await session_svc.get_session(
            app_name="Unified Agents",
            user_id=request.user_id,
            session_id=request.session_id,
        )
        if not session:
            session = await session_svc.create_session(
                app_name="Unified Agents",
                user_id=request.user_id,
                session_id=request.session_id,
            )
        logger.info("Session: %s", session)

        runner = Runner(
            agent=final_agent,
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
            user_id=request.user_id,
            session_id=request.session_id,
            new_message=user_content,
        )

        response_parts=[]

        async for event in events:
            logger.info("Event: %s", event)
            if hasattr(event, 'content') and event.content:
                if hasattr(event.content, 'parts'):
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text and not part.thought:
                            response_parts.append(part.text)
        
        response_message = "".join(response_parts).strip()
        
        return UnifiedAgentResponse(response=response_message)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    