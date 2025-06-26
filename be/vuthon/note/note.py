class Note:
    def __init__(self):
        self.notes  = ["doc-1", "doc-2", "doc-3"]

    def list(self) -> list[str]:
        return  self.notes

    def get(self, note_id: str) -> str | None:
        return next((note for note in self.notes if note == note_id), None)
