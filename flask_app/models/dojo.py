from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo():
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []

        for item in results:
            if len(dojos) == 0:
                new_dojo = Dojo(item)
                dojos.append(new_dojo)
            else:
                if item['id'] != dojos[-1].id:
                    new_dojo = Dojo(item)
                    dojos.append(new_dojo)
            if item['ninjas.id'] != None:        
                ninja_data = {
                    'id': item['ninjas.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'created_at': item['ninjas.created_at'],
                    'updated_at': item['ninjas.updated_at'],
                    'dojo_id': item['dojo_id']
                }
                new_ninja = ninja.Ninja(ninja_data)
                new_dojo.ninjas.append(new_ninja)
                new_ninja.dojo = new_dojo

        return dojos

    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(dojo_name)s);"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return results