from fastapi import FastAPI

from app.api.projects import router as project_router

app = FastAPI(
    title="PamiMai",
    version="0.1.0"
)

app.include_router(project_router)

@app.get("/")
def root():
    return {
        "name": "PamiMai",
        "version": "0.1.0",
        "status": "running"
    }