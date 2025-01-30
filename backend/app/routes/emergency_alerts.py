from fastapi import APIRouter

router = APIRouter()

@router.post("/send")
async def send_emergency_alert(patient_id: int):
    return {"message": f"Emergency alert sent for patient {patient_id}"}
