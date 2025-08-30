from flask_login import UserMixin
from app import login_manager, mysql

class User(UserMixin):
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()

    if user_data:
        return User(user_data["id"], user_data["name"], user_data["email"], user_data["password"])
    return None
