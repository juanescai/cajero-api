from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    saldo: int

database_users = Dict[str,UserInDB]

database_users = {"raul10":UserInDB(**{"username":"raul10",
                                        "password":"mintic2022",
                                        "saldo":15000}),
                   "juan20":UserInDB(**{"username":"juan20",
                                        "password":"mintic2020",
                                        "saldo":10000})  
                 }

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db

