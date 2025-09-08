from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from typing import AsyncGenerator
import os
import logging
from dotenv import load_dotenv
load_dotenv()

from routers import unified_agent

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    try:
        os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = os.getenv("GOOGLE_GENAI_USE_VERTEXAI")
        logger.info("API startup complete!!!")
        yield
        logger.info("Shutting down Application...")
    except Exception as e:
        logger.error(f"Failed to start application : {e}")
        raise

    

app = FastAPI(
    title="Unified Agents for Practice",
    description="API Interface for running the unified agents under this project.",
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(unified_agent.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Unified Agent App is Running."}