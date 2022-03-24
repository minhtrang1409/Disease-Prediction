from Models.M_Database import Database

class DB_Form(Database):
    def __init__(self):
        Database.__init__(self)

    def GetRequests(self):
        SQLquery = 'SELECT ID, phone_number, title, description, status FROM requests'
        data = Database.GetAll(self, SQLquery, ())
        return data

    def CreateRequest(self, username, form):
        SQLquery = 'INSERT INTO requests (username, phone_number, title, description, status) VALUES (%s, %s, %s, %s, %s)'
        check = Database.Execute(self, SQLquery, (username, form[0], form[1], form[2], form[3]))
        return check

    def CompleteRequest(self, ID):
        SQLquery = 'UPDATE requests SET status = %s WHERE ID = %s'
        check = Database.Execute(self, SQLquery, ("Completed", int(ID)))
        return check

    def ReportRequest(self, ID, reason):
        SQLquery = 'UPDATE requests SET status = %s, reason = %s WHERE ID = %s'
        check = Database.Execute(self, SQLquery, ("Suspend", reason, int(ID)))
        return check