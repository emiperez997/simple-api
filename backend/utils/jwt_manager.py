from jwt import encode, decode
from datetime import datetime, timedelta  # Date
from jwt.exceptions import ExpiredSignatureError


def create_token(data: dict) -> str:
    dt = datetime.utcnow() + timedelta(minutes=5)
    token: str = encode(payload={**data, **{"exp": dt}},
                        key='secret', algorithm='HS256')
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key='secret', algorithms=['HS256'])
    return data
