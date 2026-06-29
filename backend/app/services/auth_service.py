from sqlalchemy.orm import Session

from app.models.user import User
from app.auth.hashing import hash_password, verify_password
from app.auth.jwt_handler import create_access_token


class AuthService:

    @staticmethod
    def register(
        db: Session,
        full_name: str,
        email: str,
        password: str,
    ):

        exists = db.query(User).filter(
            User.email == email
        ).first()

        if exists:
            raise ValueError("Email already exists")

        user = User(
            full_name=full_name,
            email=email,
            password_hash=hash_password(password),
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str,
    ):

        user = db.query(User).filter(
            User.email == email
        ).first()

        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError("Invalid credentials")

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "role": user.role,
            }
        )

        return token