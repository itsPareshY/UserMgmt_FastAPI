from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "ABC"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# User Model
class RegisterRequest(BaseModel):
    email: str
    username: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Connect to DB
def get_db():
    conn = sqlite3.connect("users.db", check_same_thread=False)
    return conn, conn.cursor()

@router.post("/register")
def register(user: RegisterRequest):
    conn, cursor = get_db()
    hashed_password = pwd_context.hash(user.password)

    try:
        cursor.execute("INSERT INTO users (email, username, password_hash) VALUES (?, ?, ?)",
                       (user.email, user.username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email or username already exists")

    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: LoginRequest):
    conn, cursor = get_db()
    cursor.execute("SELECT password_hash FROM users WHERE email = ?", (user.email,))
    db_user = cursor.fetchone()


    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not pwd_context.verify(user.password, db_user[0]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
def logout():
    return {"message": "User logged out"}