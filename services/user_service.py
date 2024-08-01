from pymongo import MongoClient
from models.user import User
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client.fastapi_db
collection = db.users


def get_all_users():
    users = []
    for user in collection.find():

        users.append(User(**user))

    return users


def get_user(user_id):
    # to call the row object id, use below one
    user = collection.find_one({"_id": ObjectId(user_id)})
    # to call user id which is given by us, use below one
    # user = collection.find_one({"id": user_id})
    return User(**user) if user else None


def get_userbyage(age):
    user = collection.find_one({"age": age})
    return User(**user) if user else None


def create_user(user: User):
    result = collection.insert_one(user.dict())
    user.id = str(result.inserted_id)
    return user


def update_user(user_id, user: User):
    collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
    user.id = user_id
    return user


def delete_user(user_id):
    collection.delete_one({"_id": ObjectId(user_id)})
