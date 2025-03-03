class DataAuthMocks:

    data_user_create = {
        "username": "goku_user", "password": 123456, "password2": 123456, "email": "goku@gmail.com",
        "name": "goku"}

    data_user_login = {"username": "goku_user", "password": 123456}

    data_user_create_wrong = {
        "username": "",
        "password": "",
        "password2": "", }
