from flask import Flask
from database.db import initialize_db

from flask_bcrypt import Bcrypt
from flask_restful import Api
from resources.routes import initialize_routes


from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
load_dotenv()
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['JWT_SECRET_KEY']=os.getenv('JWT_SECRET_KEY')
api = Api(app)
bcrypt = Bcrypt(app)
jwt =JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)

users = {}
groups = {}
posts = {}
comments = {}




def send_notification(post):
 # Code to send email notification goes here
    pass
def delete_inactive_users():
    for user in users.values():
        if not user.groups and (datetime.now() - user.last_post_time) > timedelta(days=2):
            del users[user.email]

# def send_daily_feed():
#  for user in users.values():
#     if isinstance(user, (Admin, Moderator)):
#         activities = []
#         for group in user.groups:
#             for post in group.posts:
#                 activities.append(f'{post.author.name} posted in {group.name}: {post.title}')
#                 for comment in post.comments:
#                     activities.append(f'{comment.author.name} commented on {post.title}: {comment.content}')
#         if activities:
# # Code to send daily feed email goes here
#             pass


initialize_routes(api)
if __name__=='__main__':
    app.run()