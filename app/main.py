from fastapi import FastAPI

app = FastAPI(
    title="SQS API",
    description="API RESTful para integração com AWS SQS",
    version="1.0.0"
)

@app.get("/")
async def root():
      return {"message": "SQS API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}