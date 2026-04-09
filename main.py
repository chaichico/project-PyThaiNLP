from fastapi import FastAPI
from app.api.routes import tokenize

app = FastAPI(
    title="Thai Tokenizer API",
    description="API สำหรับแยกคำภาษาไทย (Thai Word Tokenization) โดยใช้ PyThaiNLP library",
    version="1.0.0",
)

# Include routers
app.include_router(tokenize.router)


@app.get("/", tags=["Health"])
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "Thai Tokenizer API is running"}