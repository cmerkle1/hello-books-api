from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

"""@blueprint_name.get("/endpoint/path/here") 
#.get() instance method, endpoint url of the request
def endpoint_name():
# will execute whenever a request matching the decorator is received
    my_beautiful_response_body = "Hello, World!"
    # must define a response body to return
    return my_beautiful_response_body
    # must return the HTTP response"""

@hello_world_bp.get("/")
def say_hello_world():
    return "Hello, World!"

@hello_world_bp.get("/hello/JSON")
def say_hello_json():
    return {
        "name": "Cady M",
        "message": "Hi!",
        "hobbies": ["Birdwatching", "Music", "Games"]
    }

@hello_world_bp.get("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body