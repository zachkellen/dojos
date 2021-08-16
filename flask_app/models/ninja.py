from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja():
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.dojo = None

    @classmethod
    def create_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        return results

    @classmethod
    def get_all_ninjas(cls,data):
        query = 'Select * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojo_id = %(dojo_id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        return results