
class User:
    def __init__(self,
                 username="",
                 password="",
                 email=None,
                 real_name="",
                 is_admin=False):
        self.username = username
        self.password = password
        self.email = email
        self.real_name = real_name
        self.is_admin = is_admin

    def __str__(self):
        return "User: {}, {}".format(
            self.username,
            "admin" if self.is_admin else "user"
        )

    def __repr__(self):
        pass


if __name__ == "__main__":
    user = User("Misha", "Pupkin")
    print(user)
