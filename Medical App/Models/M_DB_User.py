from Models.M_Database import Database
from Models.M_User import User
# from M_Database import Database
# from M_User import User
from configparser import ConfigParser
import urllib.request
import urllib.parse
import json

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

user_info = config_object["USERINFO"]

class DB_User(Database):
    def __init__(self):
        Database.__init__(self)

    def CheckLogin(self, user, pwd):
        SQLquery = 'SELECT * FROM users WHERE username = %s and pwd = %s'
        check = Database.GetOne(self, SQLquery, (user, pwd))
        if check != None:
            return 1
        else:
            return -1

    def CreateAccount(self, user, pwd, email):
        check = self.CheckExistence(email, 'email')
        if check == 1:
            # Email exist
            return 0
        check = self.CheckExistence(user, 'user')
        if check == 1:
            return 1
        SQLquery = 'INSERT INTO users (username, pwd, email) VALUES (%s, %s, %s)'
        Database.Execute(self, SQLquery, (user, pwd, email))
        SQLquery = 'INSERT INTO profile_user (username) VALUES (%s)'
        Database.Execute(self, SQLquery, (user,))
        return 2

    def CheckExistence(self, data, stringof):
        if stringof == 'email':
            SQLquery = "SELECT * FROM users WHERE email = %s"
        elif stringof == 'user':
            SQLquery = "SELECT * FROM users WHERE username = %s"
        check = Database.GetOne(self, SQLquery, (data,))
        if check != None:
            # Exist
            return 1
        else:
            # Not exist
            return -1

    def GetRole(self, username):
        SQLquery = 'SELECT role FROM users WHERE username = %s'
        data = Database.GetOne(self, SQLquery, (username,))
        return str(data[0])
    
    def GetStatus(self, username):
        SQLquery = 'SELECT status FROM users WHERE username = %s'
        data = Database.GetOne(self, SQLquery, (username,))
        return str(data[0])

    def GetEmail(self, username):
        SQLquery = 'SELECT email FROM users WHERE username = %s'
        data = Database.GetOne(self, SQLquery, (username,))
        return str(data[0])

    def ChangePassword(self, username, password):
        SQLquery = 'UPDATE users SET pwd = %s WHERE username = %s'
        check = Database.Execute(self, SQLquery, (password, username))
        return check

    def GetProfile(self, username):
        SQLquery = 'SELECT firstname, lastname, gender, date_of_birth, job FROM profile_user WHERE username = %s'
        data = Database.GetOne(self, SQLquery, (username,))
        lst = ["" if x is None else x for x in data]
        if lst[2] == "" or lst[2] == "Male":
            lst[2] = 0
        elif lst[2] == "Female":
            lst[2] = 1
        elif lst[2] == "Transgender":
            lst[2] = 2
        else: lst[2] = 3
        
        if lst[3] == "":
            lst[3] = "1/1/2000"
        return lst

    def UpdateProfile(self, username, array=()):
        SQLquery = 'UPDATE profile_user SET firstname = %s, lastname = %s, gender = %s, date_of_birth = %s, job = %s WHERE username = %s'
        check = Database.Execute(self, SQLquery, (array[0], array[1], array[2], array[3], array[4], username))
        return check

    def VerifyEmail(self, email):
        API_info = config_object["APIINFO"]

        data = {"email": email}
        params = json.dumps(data).encode('utf-8')

        url = API_info["JSON_URL"] + "VerifyEmail"
        req = urllib.request.Request(url, data=params, headers={'content-type': 'application/json'})

        res = urllib.request.urlopen(req)
        result = json.load(res)
        print(result['verified'])

    def SearchUsername(self, keyword):
        SQLquery = 'SELECT username, role FROM users WHERE username LIKE %s'
        keyword = "%" + keyword + "%"
        data = Database.GetAll(self, SQLquery, (keyword,))
        return data

    def UpdateStatus(self, username, status, reason):
        SQLquery = 'UPDATE users SET status = %s, reason = %s WHERE username = %s'
        check = Database.Execute(self, SQLquery, (status, reason, username))
        return check

# if __name__ == "__main__":
#     db = DB_User()
#     db.GetProfile("user")