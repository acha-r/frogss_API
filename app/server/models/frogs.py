from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"

class FrogStatus(str, Enum):
    pending = "Pending"
    eaten = "Eaten"

# Data schema for new frog creation
class FrogsSchema(BaseModel):
 name: str = Field(..., description="Enter the frog's name")
 description: str = Field(...)
 frog_status: FrogStatus
 priority: Priority
 due_date: str = Field(..., description="Due date in YYYY-MM-DD format")
 created_at: Union[datetime, None] = None
 updated_at: Union[datetime, None] = None

 class Config:
   json_schema_extra = {
     "example":[
       {
         "name":"API Assigment",
         "description":"Build a robust task management system with FastAPI",
         "frog_status":"Eaten",
         "priority":"Medium",
         "due_date": "2023-09-10",
         "created_at":"2023-09-10T23:23:35.403+00:00",
         "updated_at":"2023-09-10T23:23:35.403+00:00"
       }
     ]
   }

# Data Schema for updating a frog
class UpdateFrogsSchema(BaseModel):
 name: str = Field(...)
 description: str = Field(...)
 frog_status: FrogStatus
 priority: Priority
 due_date: str = Field(...)
 updated_at: Union[datetime, None] = None

 class Config:
  json_schema_extra = {
   "example":[
    {
     "name":"Eat that frog",
     "description":"Finish tasks on your list before COB",
     "frog_status":"Eaten or Pending",
     "priority":"High, Medium or Low",
     "due_date": "2023-09-10",
    }
   ]
  }