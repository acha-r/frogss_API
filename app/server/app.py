from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.server.api.v1.endpoints.frogs import router as FrogsRouter
from app.server.api.v1.endpoints.auth import router as AuthenticationRouter

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(AuthenticationRouter, prefix="/auth", tags=["Authentication"])
app.include_router(FrogsRouter, tags=["Eat That Frog"], prefix="/frogs")

@app.get("/")
async def frogs_app():
  content = {"Message": "Eat That Frog!"}
  return JSONResponse(content=content, status_code=status.HTTP_200_OK)
