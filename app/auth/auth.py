from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext

SECRET_KEY = "hello-from-escape-team"

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Tester
fake_users_db = {
    "frogEater": {
        "username": "frogEater",
        "password": "$2b$12$8VqqD7OcekUALxRJNggIteSo/88MEjHh4FX2PI75BhefrpY5tECE6",
        "disabled": False,
    }
}


def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not pwd_context.verify(password, user["password"]):
        return False
    return user

def create_access_token(data: dict):
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        token_data = {"username": username}
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return token_data