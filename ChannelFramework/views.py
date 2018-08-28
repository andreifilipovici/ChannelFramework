import json

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def return_manifest(request):
    with open('ChannelFramework/manifest.json') as json_data:
        data = json.load(json_data)
        return Response(data)


@api_view(['POST'])
def pull_data(request):
    with open('ChannelFramework/json_data.json') as json_data:
        data = json.load(json_data)
        return Response(data)


@api_view(['POST'])
def channel_back(request):
    return Response(request.POST)


@api_view(['GET'])
def admin_ui(request):
    admin_ui = """<html><body>
          <form method="post" action = "./admin_ui_2">
          Name: <input type="text" name="name" value="${escapeString(name)}"><br>
          Login:
          <input type="text" name="login" value="${escapeString(login)}"><br>
          Password:
          <input type="password" name="password" value="${escapeString(password)}"><br>
          WordPress location (URL):
          <input type="text" name="wordpress_location" value="${
          escapeString(location)}"><br>
          <input type="hidden" name="return_url"
               value="${escapeString(returnUrl)}"></input>
               ${warningStr}
               <input type="submit">
               </form>
           </body></html>"""
    return Response(admin_ui)
