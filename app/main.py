from fastapi import FastAPI
from app.routes import auth_router, users_router, admin_router, security_router, notifications_router
from app.database import initialize_database  # Import database initializer

app = FastAPI(title="User management API",
             description="Secure user management API for personal website",
             version="1.0.0")

# Ensure database is initialized when the app starts
initialize_database()

# Registering Routes

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(security_router, prefix="/security", tags=["Security"])
app.include_router(notifications_router, prefix="/notifications", tags=["Notifications"])

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
