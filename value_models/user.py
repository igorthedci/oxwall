
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


class Profile:
    def __init__(self,
                 username="tested_user",
                 email="qq@qq.qq",
                 password="tested",
                 real_name="tested user",
                 gender="male",
                 birthday=[1,'Jan',1991],
                 looking_for=[True,True],
                 here_for=[True,True,True,True],
                 music="music",
                 book="book"):
        self.username = username
        self.email = email
        self.password = password
        self.real_name = real_name
        self.gender = gender
        self.birthday = birthday.copy()
        self.looking_for = looking_for.copy()
        self.here_for = here_for.copy()
        self.music = music
        self.book = book

    def __str__(self):
        return "Profile: username={}, email={}".format(
            self.username, self.email
        )

    def __repr__(self):
        pass


if __name__ == "__main__":
    user = User("Misha", "Pupkin")
    profile = Profile("new_user", "new@email.com")
    print(user)
    print(profile)
