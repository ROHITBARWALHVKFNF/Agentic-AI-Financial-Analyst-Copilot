from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["API"]
)


@router.get("/info")
def info():
    return {
        "project": "AI Financial Analyst Copilot",
        "stage": "Backend Setup",
        "author": "Rohit"
    }