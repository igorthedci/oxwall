
def test_join_user(app):

    open_join_page()

    type_username('user01')
    type_email('qq@qq.qq')
    type_password('user_pw01')
    type_password2('user_pw01')
    type_realname('User')
    select_gender('male')
    select_birthday('22-may-1922')
    select_looking_for(('male', 'female'))

