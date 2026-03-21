from fastapi import FastAPI

app = FastAPI(
    title = "TaskTrack API",
    description = "A simple task management backend built with FastAPI, SQLModel etc",
    version = "1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to TaskTrack API",
        "version": app.version
    }

@app.get("/health")
def health_check():
    """Health check endpoint for load balancers and monitoring."""
    return {
        "status": "healthy",
        "version": app.version
    }

