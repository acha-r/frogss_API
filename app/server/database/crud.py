from app.server.database.database_connection import frogs
from app.server.models.frogs import FrogsSchema, UpdateFrogsSchema
from bson.objectid import ObjectId

async def create_frog_db(frog: FrogsSchema):
 frog = frog.model_dump()
 try:
  new_frog = await frogs.insert_one(frog)
  get_new_frog = await frogs.find_one({"_id": new_frog.inserted_id})
  return get_new_frog
 except Exception as e:
  return {"Error_message":str(e)}
 
async def get_single_frog_db(id: str):
 try:
  frog = await frogs.find_one({"_id":ObjectId(id)})
  if frog:
   return frog
 except Exception as e:
  return {"Error_message": str(e)}

async def get_all_frogs_db():
 frog_data = []
 try:
  get_all_frogs = frogs.find()
  if get_all_frogs:
   async for frog in get_all_frogs:
    frog_data.append(frog)
    return frog_data
 except Exception as e:
  return {"Error_message": str(e)}

async def update_single_frog_db(id: str, frog_data: UpdateFrogsSchema):
 frog = frog_data.model_dump()
 try:
  update_frog = await frogs.update_one({"_id":ObjectId(id)}, {"$set":{
   "name":frog["name"],
   "description": frog["description"],
   "priority": frog["priority"],
   "frog_status": frog["frog_status"],
   "due_date": frog["due_date"],
   "updated_at": frog["updated_at"]
 }})
  if update_frog:
   get_frog = await frogs.find_one({"_id":ObjectId(id)})
  return get_frog
 except Exception as e:
  return {"Error_message": str(e)}

async def delete_single_frog_db(id: str):
 try:
  result = await frogs.delete_one({"_id":ObjectId(id)})
  return {"message":"Successfully Deleted frog", "result":result}
 except Exception as e:
  return {"Error_message": str(e)}

async def delete_all_frogs_db():
 try:
  result = await frogs.delete_many({})
  return {"message":"All frogs deleted"}
 except Exception as e:
  return {"Error_message": str(e)}