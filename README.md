
```markdown
# 🚀 BAPMS Face Detection API

A **FastAPI**-based face recognition and attendance verification system using **DeepFace**.

---

## 🗂 Project Structure

```

bapms-face-detection/
├── app/
│   ├── controller/          # API route handlers
│   ├── services/            # Business logic and face verification code
│   │   └── face\_verifier.py
│   ├── shared/              # Shared utilities (file saving, cleanup)
│   │   └── file.py
│   ├── main.py              # FastAPI app initialization
├── temp/                    # Temporary folder for uploaded files
├── venv/                    # Python virtual environment (not included in repo)
├── .env                     # Environment variables
├── .gitignore               # Git ignore file
├── requirements.txt         # Python dependencies
├── run.py                   # Run script for uvicorn

````

---

## ✨ Features

- Upload images to verify face matches against stored employee images.
- Async file upload handling using `aiofiles`.
- Face verification done with DeepFace (**ArcFace** model).
- API documented with Swagger UI automatically by FastAPI.
- Simple cleanup of temporary files after verification.

---

## ⚙️ Setup Instructions

1. **Clone the repository**

    ```bash
    git clone https://github.com/nesuh/Attendance-Face-Verification.git
    cd Attendance-Face-Verification/bapms-face-detection
    ```

2. **Create virtual environment and activate**

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/MacOS
    venv\Scripts\activate      # Windows
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create `.env` file**

    Create a `.env` file with optional environment variables (example):

    ```env
    IMAGES_FOLDER=./uploads
    MODEL_NAME=ArcFace
    DISTANCE_METRIC=cosine
    THRESHOLD=0.40
    ```

5. **Run the API**

    ```bash
    python run.py
    ```

    The API will run on: `http://localhost:8000`

---

## 📡 API Endpoints

### POST `/api/face/verify`

Upload an image file to verify face identity.

- **Request**: `multipart/form-data` with a file field named `file`

- **Response**:

  - If matched:

    ```json
    {
      "matched": true,
      "employeeId": "123",
      "distance": 0.35
    }
    ```

  - If no match:

    ```json
    {
      "matched": false,
      "employeeId": null
    }
    ```

---

## 📚 Swagger UI

FastAPI provides interactive API docs at:

````

[http://localhost:8000/docs](http://localhost:8000/docs)

```

You can test the `/api/face/verify` endpoint directly from this UI.

---

## 📝 Notes

- Temporary uploaded files are saved in the `temp/` directory and cleaned up automatically.
- Stored employee images should be placed inside the folder configured in `.env` (`IMAGES_FOLDER`).
- DeepFace configuration can be adjusted using environment variables.

---

## 📄 License

MIT License

---

## 📬 Contact

For questions, reach out to the maintainer.
```

