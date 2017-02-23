import pecan
import uuid
from pecan import rest, response, request
from deployerengine.model import Session
from deployerengine.model.Jobs import Jobs

class VersionController(rest.RestController):

    @pecan.expose("json")
    def get(self, id):
        return { "name" : id }

    @pecan.expose("json")
    def post(self):
        data = request.json
        #validate data
        id = uuid.uuid4().hex
        p = Jobs(id,data["NumServer"])
        s = Session()
        s.add(p)
        s.commit()
        response.status = 201
        return id
    
    @pecan.expose("json")
    def put(self):
        response.status = 204
        return 
    
    @pecan.expose("json")
    def delete(self):
        response.status = 200
        return

