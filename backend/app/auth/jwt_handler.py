from datetime import datetime, timedelta

from jose import jwt

from app.config import settings


SECRET_KEY = settings.JWT_SECRET
ALGORITHM = settings.JWT_ALGORITHM


def create_access_token(data: dict, expires_minutes: int = 60):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)

    payload["exp"] = expire

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str):
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
    )