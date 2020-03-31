from django.test import TestCase

# Create your tests here.
import requests

# "/text/t1"
#
# {
#     "name":mm
# }
#
#
# {
#     "shwiud"
# }
#  requests.post(url)
import json
data={
    "name":"admin",
    "abc":"cheng123"
}
request = requests.get("http://121.12.85.154:7080/auth/login", data=json.dumps(data))
print(request.content)