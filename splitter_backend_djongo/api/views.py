import json

import database
from django.http import JsonResponse

# Create your views here.
db = database.DataBase()



def get_Everything(request):
    val = db.getAllUserData()
    return JsonResponse(json.dumps(val[0], default=str), safe=False)

def get_UserData(request, username):
    val = db.findUserByField("username", username)
    if not val[0] == None:
        return JsonResponse(json.dumps(val[0], default=str), safe=False)
    else:
        return JsonResponse({"Error": "No User found for " + username })