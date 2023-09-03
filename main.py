from fastapi import FastAPI, UploadFile, File,  Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.post("/documents")
async def create_file(title: Annotated[str, Form()], file: Annotated[UploadFile, File()],):
    return {"title": title, "file_size": file.content_type}
