# hash imports
import hashlib

# for .env imports
import os
from dotenv import load_dotenv
load_dotenv()


def hashing(password, user_id):
    ''' Foo hashs password entered by user '''

    print('come here')
    user_id = str(user_id)
    password_start = os.getenv('PASSWORD_START')
    password_finish = os.getenv('PASSWORD_FINISH')
    HASH_ALGO = os.getenv('CUSTOM_HASH_ALGO')

    password = password_start + password + str(user_id[3:7]) + password_finish
    password = password.encode('utf-8')
    password = hashlib.new(HASH_ALGO, password).hexdigest()
    salt = password[3:6]
    salt = salt.encode('utf-8')
    password = password.encode('utf-8')
    hashed_password = hashlib.pbkdf2_hmac(
            hash_name=HASH_ALGO, password=password, salt=salt, iterations=100000)
    print(hashed_password)
    return (hashed_password.hex())