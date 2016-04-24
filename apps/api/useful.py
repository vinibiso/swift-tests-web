# Python
import json
# Django
from django.http import HttpResponse

def make_response(dict):
    response = HttpResponse(json.dumps(dict, sort_keys=True, indent=4))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
