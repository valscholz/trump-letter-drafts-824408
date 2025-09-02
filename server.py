#!/usr/bin/env python3
"""Web server template for Caminu-generated agents"""

import asyncio
import os
import logging
from typing import Any, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from agent import agent
from agents import Runner

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Trump-Style Letter Generator (Safety-Compliant)",
    description="Users want to generate persuasive, high-energy letters inspired by the rhetorical style often associated with Donald Trump for a user-provided topic. The agent must produce content that captures high-level stylistic characteristics while avoiding direct impersonation, exact pastiche, or policy-violating political persuasion, ensuring clarity, safety, and usefulness in a single interaction.",
    version="1.0.0"
)

class AgentRequest(BaseModel):
    prompt: str = "Please demonstrate your functionality."

class AgentResponse(BaseModel):
    response: str
    status: str = "success"

@app.get("/")
async def root():
    return {
        "message": "Welcome to Trump-Style Letter Generator (Safety-Compliant)",
        "endpoints": {
            "POST /generate": "Generate a response from a prompt",
            "GET /health": "Health check"
        }
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "trump-style-letter-generator-safety-compliant"}

@app.post("/generate", response_model=AgentResponse)
async def generate(request: AgentRequest):
    try:
        logger.info(f"Processing request: {request.prompt[:100]}...")
        result = await Runner.run(agent, request.prompt)
        return AgentResponse(
            response=result.final_output,
            status="success"
        )
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting server on port {port}")
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=port,
        log_level="info"
    )