from fastapi import FastAPI, APIRouter
from .note import Note

app = FastAPI()
router = APIRouter()
note = Note()

@router.get("/", tags=["Note"], description="List all notes in the database.")
async def note_list() -> list[str]:
    return note.list()

@router.get("/{note_id}", tags=["Note"], description="Get a note by its ID.")
async def note_get(note_id: str) -> str:
    return note.get(note_id=note_id)

app.include_router(router)
