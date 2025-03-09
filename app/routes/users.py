from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/me")
def get_user_profile(user_email: str = Depends(get_current_user)):
    return {"message": f"Welcome {user_email}, this is your profile"}

@router.put("/update")
def update_profile():
    return {"message": "User profile updated"}

@router.delete("/delete")
def delete_user():
    return {"message": "User account deleted"}
