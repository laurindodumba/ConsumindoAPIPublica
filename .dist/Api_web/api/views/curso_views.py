from flask_restful import Resource
from app import api



class CursoList(Resource):
    def get(self):
        return "Olá mundo"


api.add_resource(CursoList, '/curso')