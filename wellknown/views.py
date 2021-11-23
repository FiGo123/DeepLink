from django.shortcuts import render
import json
from django.http import HttpResponse, response

# Create your views here.
def say_hello(request):
    response = [{
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
    "namespace": "android_app",
    "package_name": "com.pro.launcher",
    "sha256_cert_fingerprints": ["9F:17:51:65:4D:C2:EE:71:21:79:DA:CD:7A:B5:1A:32:79:8F:88:58:24:CB:45:2D:D9:F6:7D:BC:25:D0:83:DD"]
  }
}]
    return HttpResponse(json.dumps(response))