from fastapi import APIRouter

router = APIRouter()

@router.post("/consult")
async def start_consultation(patient_id: int):
    return {"message": f"Telemedicine session started for patient {patient_id}"}
