from fastapi import FastAPI, Depends, status,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing_extensions import Annotated
import models, auth
from database import db_dependency, engine
from schemas import NotesRequest
from database import get_db
from models import Note

app = FastAPI(title="Notes Application")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Development
        "http://127.0.0.1:3000",  # Development
        "https://python-keeps-7oun87pqt-pritammishra065s-projects.vercel.app/login",  # Replace with your Vercel domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)

# Create all tables
models.Base.metadata.create_all(bind=engine)


@app.get("/", status_code=status.HTTP_200_OK)
async def read_current_user(
   current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db),
):
    return {"user": current_user}


@app.post("/notes/save", status_code=status.HTTP_201_CREATED)
async def save_note(
    note:NotesRequest,
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db),
):
    saved_note = Note(
        title=note.title,
        content=note.content,
        user_id=current_user["id"],
    )
    db.add(saved_note)
    db.commit()
    db.refresh(saved_note)
    return {"note_id": saved_note.id, "title": saved_note.title, "content": saved_note.content}

@app.get("/notes", status_code=status.HTTP_200_OK)
async def get_user_notes(
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db),
):
    notes = db.query(Note).filter(Note.user_id == current_user["id"]).all()
    return [{"id": note.id, "title": note.title, "content": note.content} for note in notes]

@app.delete("/notes/delete/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(
    note_id: int,
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db),
):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user["id"]).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or unauthorized")

    db.delete(note)
    db.commit()
    return

@app.delete("/notes/delete/{title}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(
    title:str,
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db),
):
    note = db.query(Note).filter(Note.title == title, Note.user_id == current_user["id"]).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found or unauthorized")

    db.delete(note)
    db.commit()
    return