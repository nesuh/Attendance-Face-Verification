import os
from uuid import uuid4
import aiofiles

TEMP_FOLDER = "temp"
os.makedirs(TEMP_FOLDER, exist_ok=True)

async def save_temp_file(file) -> str:
    """Save uploaded file asynchronously to a temporary folder."""
    file_ext = os.path.splitext(file.filename)[1]
    temp_path = os.path.join(TEMP_FOLDER, f"{uuid4()}{file_ext}")

    async with aiofiles.open(temp_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    return temp_path

def cleanup_file(path: str):
    """Delete a temporary file if it exists."""
    if os.path.exists(path):
        os.remove(path)
