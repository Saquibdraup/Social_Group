from .SocialGroup import UsersApi, UserApi
def initialize_routes(api):
    api.add_resource(UserApi, '/api/SG')
    api.add_resource(UsersApi, '/api/SG/<id>')













# # Routes to create a new user
# @app.route('/users', methods=['POST'])
# def create_user():
#  data = request.get_json()
#  email = data['email']
#  if email in users:
#  return jsonify({'error': 'User with email already exists'}), 409
#  user = User(data['name'], email, data['password'])
#  users[email] = user
#  return jsonify({'message': 'User created successfully'}) 
# # Routes to create a new group
# @app.route('/groups', methods=['POST'])
# def create_group():
#  data = request.get_json()
#  name = data['name']
# admin_email = data['admin']
# if admin_email not in users:
#  return jsonify({'error': 'Admin not found'}), 404
#  admin = users[admin_email]
# group = Group(name, admin