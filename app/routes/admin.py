from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/users")
def list_users():
    return {"message": "List of all users (Admin only)"}

@router.put("/users/{user_id}/role")
def update_user_role(user_id: int):
    return {"message": f"Updated role for user {user_id}"}

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"Deleted user {user_id}"}
