import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LOCAL_NOTES")

home_dir = os.path.expanduser("~")
notes_path = os.path.join(home_dir, "notes.txt")

@mcp.tool()
def add_notes_to_file(content: str) -> str:
    """
    Appends the given content to notes.txt in the user's home directory.
    Creates the file if it does not exist.
    """
    try:
        file_created = False
        if not os.path.exists(notes_path):
            # Ensure file is created before writing
            open(notes_path, "w", encoding="utf-8").close()
            file_created = True

        with open(notes_path, "a", encoding="utf-8") as f:
            f.write(content + "\n")

        if file_created:
            return f"🆕 File created at {notes_path} and content appended."
        else:
            return f"✅ Content appended to {notes_path}"

    except Exception as e:
        return f"❌ Error appending to file {notes_path}: {e}"

@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the contents of notes.txt in the user's home directory.
    Always shows the file path.
    """
    try:
        if not os.path.exists(notes_path):
            return f"⚠️ No notes file found at {notes_path}"
        with open(notes_path, "r", encoding="utf-8") as f:
            notes = f.read()
        if notes:
            return f"📂 Notes file path: {notes_path}\n\n📝 Contents:\n{notes}"
        else:
            return f"📂 Notes file path: {notes_path}\n\n⚠️ No notes found!"
    except Exception as e:
        return f"❌ Error reading from file {notes_path}: {e}"
