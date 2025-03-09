from fastapi import APIRouter

router = APIRouter()

@router.post("/reset-password")
def reset_password():
    return {"message": "Password reset requested"}

@router.post("/change-password")
def change_password():
    return {"message": "Password changed successfully"}

@router.get("/rate-limit-check")
def rate_limit_check():
    return {"message": "Rate limit check successful"}