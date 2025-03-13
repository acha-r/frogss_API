from fastapi import APIRouter, status, HTTPException, Depends, Form, Body
from app.auth.auth import get_current_user
from app.server.models.frogs import FrogsSchema
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime, time, timedelta
from typing import Annotated, Any, List
from bson.objectid import ObjectId
from app.server.models.frogs import FrogStatus, Priority

from app.server.database.crud import (
 create_frog_db,
 get_single_frog_db,
 get_all_frogs_db,
 update_single_frog_db,
 delete_single_frog_db,
 delete_all_frogs_db
)
from app.server.database.database_connection import frogs
from app.server.models.frogs import (
 FrogsSchema,
 UpdateFrogsSchema
)
router = APIRouter(
    dependencies=[Depends(get_current_user)])

# Create frog
@router.post("/", response_model=FrogsSchema, response_description="Creating A frog")
async def create_frog(name: Annotated[str, Form(description="Enter the frog's name")],
                      description: Annotated[str, Form(description="Provide a brief description")],
                      frog_status: Annotated[FrogStatus, Form()],
                      priority: Annotated[Priority, Form()],
                      due_date: Annotated[str, Form(description="Due date in DD-MM-YYYY format")]) -> Any:
 try:
  created_at = datetime.now()
  frog = FrogsSchema(
   name=name,
   description=description,
   frog_status=frog_status,
   priority=priority,
   due_date=due_date,
   created_at=created_at,
   updated_at=None
  )
  new_frog = await create_frog_db(frog)
  response = {
   "id": str(new_frog["_id"]),
   "message": "frog Created Successfully"
  }

  response = jsonable_encoder(response)
  return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)
 except Exception as e:
  raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
 
 #Get all frogs
@router.get("/", response_model=List[FrogsSchema], response_description="Get all frogs")
async def get_all_frogs():
    all_frogs_list = []
    try:
        get_all_frogs = await get_all_frogs_db()
        if get_all_frogs:
            for frog in get_all_frogs:
                frog_data = FrogsSchema(
                    name=frog["name"],
                    description=frog["description"],
                    frog_status=frog["frog_status"],
                    priority=frog["priority"],
                    due_date=frog["due_date"],
                    created_at=frog["created_at"],
                    updated_at=frog["updated_at"]
                )
                all_frogs_list.append(frog_data)
        
        response = jsonable_encoder(all_frogs_list)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
 
 #Get one frog
@router.get("/{id}", response_model=FrogsSchema, response_description="Get Single frog")
async def get_single_frog(id: str):
    try:
        get_frog = await get_single_frog_db(id)

        if not get_frog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Frog not found. Please check the ID and try again."
            )

        response = FrogsSchema(
            name=get_frog["name"],
            description=get_frog["description"],
            frog_status=get_frog["frog_status"],
            priority=get_frog["priority"],
            due_date=get_frog["due_date"],
            created_at=get_frog["created_at"],
            updated_at=get_frog["updated_at"]
        )

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

    except HTTPException as http_exc:
        raise http_exc

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Frog not found. Please check the ID and try again."
        )
 
 #Update a frog
@router.put("/{id}", response_model=FrogsSchema, response_description="Update Single frog")
async def update_single_frog(id: str, frog: UpdateFrogsSchema = Body(...)):
 try:
  frog = frog.model_dump()
  updated_at = datetime.now()
  updated_frog = UpdateFrogsSchema(
   name=frog['name'],
   description=frog['description'],
   frog_status=frog['frog_status'],
   priority=frog['priority'],
   due_date=frog['due_date'],
   updated_at=str(updated_at)
  )
  update_frog = await update_single_frog_db(id, updated_frog)
  if update_frog:
   response = FrogsSchema(
    name=update_frog["name"],
    description=update_frog["description"],
    frog_status=update_frog["frog_status"],
    priority=update_frog["priority"],
    due_date=update_frog["due_date"],
    created_at=update_frog["created_at"],
    updated_at=update_frog["updated_at"]
   )
   response = jsonable_encoder(response)
   return JSONResponse(content=response, status_code=status.HTTP_200_OK)
 except Exception as e:
  raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

#Delete a frog
@router.delete("/{id}", response_description="Delete a Single frog")
async def delete_single_frog(id: str):
 try:
  delete_frog = await delete_single_frog_db(id)
  response = {"Message": f"frog is Successfuly Deleted!!"}
  response = jsonable_encoder(response)
  return JSONResponse(content=response, status_code=status.HTTP_200_OK)
 except Exception as e:
  raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
 
 #Delete all frogs
@router.delete("/", response_description="Delete all frogs")
async def delete_all_frogs():
 try:
  delete = await delete_all_frogs_db()
  response = {"Message": f"All frogs Successfuly Deleted!!"}
  response = jsonable_encoder(response)
  return JSONResponse(content=response, status_code=status.HTTP_200_OK)
 except Exception as e:
  raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

