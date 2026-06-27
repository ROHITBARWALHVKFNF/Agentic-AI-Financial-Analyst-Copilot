from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.routes import router as api_router
from app.api.upload import router as upload_router

app = FastAPI(
    title="AI Financial Analyst Copilot",
    description="An Agentic AI platform for financial analysis using RAG and LangGraph.",
    version="1.0.0"
)

# Register Routers
app.include_router(health_router)
app.include_router(api_router)
app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Financial Analyst Copilot",
        "version": "1.0.0",
        "status": "Running"
    }