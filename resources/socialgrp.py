from flask_restful import Resource,request
from database.models import User, Groups, Posts, Comment
from flask import request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

class GroupApi(Resource):
    def get(self):
        S_Group=Groups.objects().to_json()
        return Response(S_Group, mimetype="application/json", status=200)
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        S_Group = Groups(**body, added_by=user)
        S_Group.save()
        user.update(push__groups=S_Group)
        user_email=user.email
        S_Group.admins.append(str(user_email))
        user.save()
        id = S_Group.id
        return {'id',id}, 200

class GroupsApi(Resource):
    @jwt_required()
    def put(self,id):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        S_Group=Groups.objects.get(id=id)
        body = request.get_json()
        Groups.objects.get(id=id).update(**body)
        return '', 200


    @jwt_required()
    def delete(self,id):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        S_Group = Groups.objects.get(id=id)
        Groups.object.get(id=id).delete()
        return '', 200

    def get(self, id):
        S_Group = Groups.objects.get(id=id).to_json()
        return Response(S_Group, mimetype="application/json", status=200)






