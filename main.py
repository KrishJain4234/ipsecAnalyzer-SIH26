from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.protocol import router as protocol_router

app = FastAPI(
    title="Cyber Sentinel — Protocol Identification Service",
    description="Core Feature 1: AI-Assisted IPsec VPN Protocol Identification & Deep Dissection Engine",
    version="1.0.0",
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(protocol_router)


@app.get("/health", tags=["Health Check"])
def health_check():
    return {
        "status": "operational",
        "service": "Cyber Sentinel Protocol Identification Engine",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
