from pydantic import BaseModel, Field # Types
from typing import Optional, List # Types

# Model Task
class Task(BaseModel):
    id: Optional[int] = Field(ge=1, le=1000)
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=50)
    done: Optional[bool] = Field(default=False)

    class Config():
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Task One",
                "description": "This is task one",
                "done": False
            }
        }