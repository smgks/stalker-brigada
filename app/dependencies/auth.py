from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import ValidationError
from app.core import ALGORITHM, Settings
from app.schemas import TokenPayload
from .db import SessionDep
from app.models import User

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/auth/token"
)


async def get_token(token: str | None):
    if not token:
        raise HTTPException(status_code=400, detail="Token missing")
    # Here, add your logic to validate the token.
    return token


TokenDep = Annotated[str, Depends(reusable_oauth2)]
TokenStupidDep = Annotated[str, Depends(get_token)]


async def get_current_user(session: SessionDep, token: TokenStupidDep) -> User:
    try:
        payload = jwt.decode(
            token, Settings.SECRET_KEY, algorithms=[ALGORITHM],
        )
        token_data = TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(User, token_data.sub)
    if not User:
        raise HTTPException(status_code=404, detail="User not found")
    return user


UserDep = Annotated[str, Depends(get_current_user)]

