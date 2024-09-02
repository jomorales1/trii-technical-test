from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from app.config import settings
from app.routers.search import search

# Create FastAPI instance
app = FastAPI(
    title="Trii Technical Test API",
    description="API for querying data from a third party service",
    version="0.1.0",
    root_path=settings.root_path,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    search.router,
    prefix="/v1",
    tags=["search"],
)

# Add sample route
@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )