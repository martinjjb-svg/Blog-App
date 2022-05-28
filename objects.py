# from app import bcrypt


class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.id = id

    def __str__(self):
        return f"{self.username}: {self.email} {self.password} "

    def to_dict(self):
        return {'username': self.username, 'email': self.email, 'password': self.password}

    """
    def hash_password(self):
        return bcrypt.generate_password_hash(self.password).decode('utf-8')
    """


class Post:

    def __init__(self, id, title, date_posted, content, user_id):
        self.id = id
        self.title = title
        self.date_posted = date_posted
        self.content = content
        self.user_id = user_id

    def __str__(self):
        return f"{self.id}: {self.title} {self.date_posted} {self.content} {self.user_id}"

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'date_posted': self.date_posted, 'content': self.content,
                'user_id': self.user_id}

