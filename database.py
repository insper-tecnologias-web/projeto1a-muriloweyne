import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database():
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect("{DB_NAME}.db".format(DB_NAME=db_name))
        self.table = self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL);")

    def add(self, note):
        self.conn.execute("INSERT INTO note (title, content) VALUES (?, ?)", (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        notes_list = []
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        for line in cursor:
            note = Note(line[0], line[1], line[2])
            notes_list.append(note)
        return notes_list

    def update(self, entry):
        self.conn.execute("UPDATE note SET title = ?, content = ? WHERE id = ?", (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id = ?", (note_id,))
        self.conn.commit()


  

    
