from database.models import Comment
from flask import request, Response
from flask_restful import Resource

class CommentsApi(Resource):
    def get(self):
        comments = Comment.objects().to_json()
        return Response(comments,mimetype="application/json",status=200)

    def post(self):
        body = request.get_json()
        comments = Comment(**body).save()
        id=comments.id
        return {'id': id}, 200

class PostsApi(Resource):
    def put(self,id):
        comments = Comment.objects.get(id=id)
        body=request.get_json()
        Comment.objects.get(id=id).update(**body)
        return '', 200

    def delete(self,id):

        comments = Comment.objects.get(id=id)
        comments.delete()
        return '', 200