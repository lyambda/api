# ********** DataBase module *****************
from mod.db import create_session
from mod.api import User
# ******** End DataBase module ***************

# ************** Standart module *********************
import random
from mod.utils import email
# ************** Standart module end *****************

# Authorization
class Auth():
    def _createUser(data):
        session = create_session()
        user = User(
                name=data.ame,
                email=data.email,
                date=data.date,
                friends=data.friends,
                data=data.data
        )
        session.add(user)
        session.commit()

    def _get_user(id):
        session = create_session()
        user_all = session.query(User).all()

        for user in user_all:
            if str(user.id) == str(id):
                result = User(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    date=user.date,
                    friends=user.friends,
                    data=user.data
                )
                return result

    def login(data):
        pass

    def register():
        pass

    def sendCode(data):
        code = random.randint(100000, 999999)
        user = {
            'name': '',
            'email': data['email'],
            'date': '',
            'friends': '',
            'data': '[{"code": '+str(code)+'}]'
        }
        Auth._createUser(user)
        email(data)

    def checkCode(data):
        user = Auth._get_user(data['id'])
        return str(data['code']) == str(user.code)

    def checkToken(data):
        user = Auth._get_user(data['id'])
        return user.token == data['token']
