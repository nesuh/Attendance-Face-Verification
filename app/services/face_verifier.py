import os
import logging
import asyncio
from concurrent.futures import ThreadPoolExecutor
from deepface import DeepFace
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("face_verifier")
logger.setLevel(logging.INFO)

IMAGES_FOLDER = os.getenv("IMAGES_FOLDER", "./uploads")
MODEL_NAME = os.getenv("MODEL_NAME", "ArcFace")
DISTANCE_METRIC = os.getenv("DISTANCE_METRIC", "cosine")
THRESHOLD = float(os.getenv("THRESHOLD", 0.40))

executor = ThreadPoolExecutor(max_workers=2)

def _sync_verify_face(input_image_path: str):
    """Blocking call to DeepFace verify, run in executor"""
    if not os.path.exists(input_image_path):
        return {"matched": False, "employeeId": None, "reason": "input_not_found"}

    for fname in os.listdir(IMAGES_FOLDER):
        ref_path = os.path.join(IMAGES_FOLDER, fname)
        if not os.path.isfile(ref_path):
            continue

        employee_id = os.path.splitext(fname)[0]
        try:
            result = DeepFace.verify(
                img1_path=input_image_path,
                img2_path=ref_path,
                model_name=MODEL_NAME,
                distance_metric=DISTANCE_METRIC,
                detector_backend='retinaface',
                enforce_detection=False
            )

            distance = result.get("distance") or result.get(DISTANCE_METRIC)
            if distance is not None and distance <= THRESHOLD:
                logger.info(f"Match found: {employee_id} dist={distance}")
                return {"matched": True, "employeeId": employee_id, "distance": float(distance)}

            elif result.get("verified"):
                logger.info(f"Verified by boolean for {employee_id}")
                return {"matched": True, "employeeId": employee_id}

        except Exception as e:
            logger.exception(f"Error verifying against {ref_path}: {e}")
            continue

    return {"matched": False, "employeeId": None}

async def verify_face(input_image_path: str):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, _sync_verify_face, input_image_path)
