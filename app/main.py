from fastapi import FastAPI
from app.api.routes import health, chat, info

app = FastAPI(title="AI Knowledge Assistant", version="0.1.0")

app.include_router(health.router)
app.include_router(chat.router)
app.include_router(info.router)
