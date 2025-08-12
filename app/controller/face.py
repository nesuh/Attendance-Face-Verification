from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.face_verifier import verify_face
from app.shared.file import save_temp_file, cleanup_file

router = APIRouter()

@router.post("/verify")
async def verify_endpoint(file: UploadFile = File(...)):
    temp_path = await save_temp_file(file)
    try:
        result = await verify_face(temp_path)
        print("Face verification result:", result)  # debug in terminal

        if not result.get("matched"):
            return {"matched": False, "employeeId": None}
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cleanup_file(temp_path)
