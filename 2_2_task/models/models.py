from pydantic import BaseModel, Field, field_validator
from starlette.authentication import requires


class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)
    @field_validator("message")
    @classmethod
    def check_forbidden_words(cls, value: str) -> str:
        forbidden_words = ["кринж", "рофл", "вайб"]
        message_lower = value.lower()
        for word in forbidden_words:
            if word in message_lower:
                raise ValueError("Исользование недопустимых слов")
        return value