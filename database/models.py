from .db import db
from flask_bcrypt import generate_password_hash,check_password_hash
import kwargs


class User(db.Document):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, Unique=True)
    password = db.StringField(required=True, min_length=8)
    groups = db.ListField(db.StringField, required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Groups(db.Document):
    Grp_name = db.StringField(required=True, unique=True)
    admins = db.ListField(db.StringField, required=True)
    moderators = db.ListField(db.StringField, required=True)
    members = db.ListField(db.StringField, required=True)
    type = db.StringField(choices=('PUBLIC', 'PRIVATE'), default='PUBLIC')
    posts = db.ListField(db.StringField, required=True)
    pending_post = db.ListField(db.StringField, required=True)
    pending_comments = db.ListField(db.StringField, required=True)

    def add_admin(self,admin):
        self.admins.append(admin)

    def add_moderator(self, moderator):
        self.moderators.append(moderator)

    def add_member(self, member):
        self.members.append(member)

    def remove_admin(self, admin):
        self.admins.remove(admin)

    def remove_moderator(self, moderator):
        self.moderators.remove(moderator)

    def remove_member(self, member):
        self.members.remove(member)

    def is_member(self, user):
        return user in self.members


class Role(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()
    groups = db.ListField(db.ReferenceField('Groups'))


class Posts(db.Document):

    title = db.StringField(required=True, Unique=True)
    content = db.StringField(required=True)
    author = db.StringField(required=True, Unique=True)
    group = db.StringField(required=True, Unique=True)
    comments = db.ListField(db.StringField, required=True)
    Date_Time = db.DateTimeField(required=True)

    def add_comment(self, comment):
        self.comments.append(comment)


class Comment(db.Document):

    content = db.StringField(required=True, Unique=True)
    C_author = db.StringField(required=True, Unique=True)
    C_post = db.StringField(required=True, Unique=True)
    C_Date_Time = db.DateTimeField(required=True)


