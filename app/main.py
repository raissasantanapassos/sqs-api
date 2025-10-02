from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="API RESTful para integração com AWS SQS",
    version="1.0.0",
    debug=settings.debug,
)

@app.get("/")
async def root():
      return {"message": settings.app_name,
          "docs": "/docs",
          "health": "/health"        
      }

@app.get("/health")
async def health_check():
    return {"status": "healthy",
            "service": settings.app_name,
            "version": "1.0.0",
            "debug": settings.debug,}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.host,  # ← Usa configuração
        port=settings.port   # ← Usa configuração
    )