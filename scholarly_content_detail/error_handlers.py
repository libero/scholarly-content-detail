from flask import json


def http_error_handler(error):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = error.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "type": error.code,
        "title": error.name,
        "detail": error.description,
    })
    response.content_type = "application/problem+json"
    return response
