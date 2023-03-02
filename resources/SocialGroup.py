from flask_restful import Resource
from database.models import User, Groups, Posts, Comment
from flask import request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

class UserApi(Resource):
    def get(self):
        users=User.object().to_json()
        return Response(users, mimetype="application/json", status=200)
    @jwt_required()
    def post(self):
        admin = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=admin)
        user = User(**body, added_by=user)
        user.save()
        user.update(push__users=user)
        user.save()
        id = user.id
        return {'id', str(id)}, 200
    def post_content(self):
        post = request.get_json()
        Posts.append(post)
        return {post}, 200
    def post_comment(self):
        comment=request.get_json()
        Comment.append(comment)
        return {comment}, 200
class UsersApi(Resource):
    @jwt_required()
    def put(self,id):
        user_id = get_jwt_identity()
        user = User.objects.get(id=id, added_by=user_id)
        user=request.get_json()
        User.objects.get(id=id).update(**user)
        return '', 200

    @jwt_required()
    def delete(self,id):
        user_id = get_jwt_identity()
        user = User.objects.get(id=id, added_by=user_id)
        user.delete()
        return '', 200
    def put_post(self, id):
        post=Posts.objects.get(id=id)
        post=request.get_json()
        Posts.objects.get(id=id).update(**post)
        return '', 200

    def put_comments(self, id):
        comment=Comment.get(id=id)
        comment=request.get.json()
        Comment.objects.get(id=id).update(**comment)
        return '', 200

    def delete_post(self, id):
        post=Posts.objects.get(id=id)
        post.delete()
        return '', 200

    def delete_comment(self,id):
        comment=Comment.objects.get(id=id)
        comment.delete()
        return '', 200




