
# structure of user record
#  - username: string
#  - password: string
#  - highscore: int
#  - admin: boolean

def load_user_data():
    users = []
    users.append({"username": "Alice", 
                  "password": "password", 
                  "highscore": 1000, 
                  "admin": False, })
    users.append({"username": "Bob", 
                  "password": "password", 
                  "highscore": 2000, 
                  "admin": False, })
    users.append({"username": "Charles", 
                  "password": "password", 
                  "highscore": 3000, 
                  "admin": False, })
    users.append({"username": "Doug", 
                  "password": "password", 
                  "highscore": 4000, 
                  "admin": True, })                  

    return users