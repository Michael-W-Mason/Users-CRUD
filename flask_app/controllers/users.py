from config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def create_new(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        result = connectToMySQL("user_schema").query_db(query, data)
        return result;
    
    @classmethod
    def get_one(cls, id):
        query = f"SELECT * FROM users WHERE users.id = {id}"
        result = connectToMySQL('user_schema').query_db(query)
        return result[0]
    
    @classmethod
    def get_last_one(cls):
        query = f"SELECT * FROM users ORDER BY users.id DESC LIMIT 1"
        result = connectToMySQL('user_schema').query_db(query)
        return result[0]

    @classmethod 
    def edit_one(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id=%(id)s"
        result = connectToMySQL("user_schema").query_db(query, data)
        return result

    @classmethod
    def delete_one(cls, id):
        query = f"DELETE FROM users WHERE id = {id}"
        result = connectToMySQL("user_schema").query_db(query)
        return result;
