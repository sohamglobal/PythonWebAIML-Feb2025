# pip install flask_restful
from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class BasicREST(Resource):
    def get(self):
        profile={
            "name":"praffull",
            "dob":"9 june",
            "city":"london",
            "language":"english",
            "qualification":"mba (mc)",
            "experience":"20 years",
            "keyskills":["java","spring","sql","cloud","ai"],
            "occupation":"java developer"
        }
        return profile

api.add_resource(BasicREST,"/profile")
app.run(debug=True)