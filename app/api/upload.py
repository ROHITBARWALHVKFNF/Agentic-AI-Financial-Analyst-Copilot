from fastapi import APIRouter, UploadFile, File

from app.utils.file_utils import save_uploaded_file
from app.services.pdf_service import extract_text

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = save_uploaded_file(file)

    text = extract_text(file_path)

    return {
        "filename": file.filename,
        "saved_path": file_path,
        "characters": len(text),
        "preview": text[:1000]
    }