import time

import jwt
from decouple import config

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")


class AuthHandler(object):

    @staticmethod
    def sign_jwt(user_id: int, cargo: str | None = None) -> str:
        payload = {
            "user_id": user_id,
            "cargo": cargo,
            "expires": time.time() + 900
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return token

    @staticmethod
    def decode_jwt(token: str) -> dict:
        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return decoded_token if decoded_token["expires"] >= time.time() else None
        except Exception:
            return None
