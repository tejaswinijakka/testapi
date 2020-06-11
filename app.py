from flask import Flask
from flask_restful import Api
import pymysql
from resources.emp import Emp 

app=Flask(__name__)
api = Api(app)

api.add_resource(Emp,'/emp')

app.run(port="8055",debug=True)