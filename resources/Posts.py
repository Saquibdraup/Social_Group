from database.models import Posts
from flask import request, Response
from flask_restful import Resource

class PostApi(Resource):
    def get(self):
        posts = Posts.objects().to_json()
        return Response(posts,mimetype="application/json",status=200)

    def post(self):
        body = request.get_json()
        posts = Posts(**body).save()
        id=posts.id
        return {'id': id}, 200

class PostsApi(Resource):
    def put(self,id):
        posts = Posts.objects.get(id=id)
        body=request.get_json()
        Posts.objects.get(id=id).update(**body)
        return '', 200

    def delete(self,id):

        posts = Posts.objects.get(id=id)
        posts.delete()
        return '', 200