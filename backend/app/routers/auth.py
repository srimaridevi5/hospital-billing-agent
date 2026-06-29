from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)
from app.services.auth_service import AuthService
from app.auth.dependencies import get_current_user
print(">>> AUTH ROUTER IMPORTED <<<")
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    try:
        user = AuthService.register(
            db,
            request.full_name,
            request.email,
            request.password,
        )

        return {
            "message": "User created successfully",
            "user_id": str(user.id),
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )



@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    try:
        token = AuthService.login(
            db,
            form_data.username,   # username field contains the email
            form_data.password,
        )

        return TokenResponse(
            access_token=token
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )

@router.get("/me")
def current_user(
    user=Depends(get_current_user),
):
    return user
