from google.cloud import storage
import uuid
import hashlib
from ast import literal_eval


# Get the bucket file
def read_file(filename):
    client = storage.Client.from_service_account_json("isobel-service-account-key.json")
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    bucket = client.get_bucket('tfl_bike')
    # Then do other things...
    blob = bucket.get_blob(filename)
    blob = blob.download_as_string()  # read content from bucket and print to stdout
    cred = literal_eval(blob.decode())
    return cred


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
