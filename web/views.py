from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(request):
    import requests
    import json
    # get_request = request.POST['user']
    api_request = requests.get("https://api.github.com/users?since=155")
    api = json.loads(api_request.content)
    print(api)
    # return render(request, 'home.html', {"api": get_request})
    return render(request, 'home.html', {"api": api})
    # return render(request, 'home.html', {})
def user(request):
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/"+user)
        username = json.loads(user_request.content)
        return render(request, 'user.html', {"user": user, "username": username})
    else:
        notfound = "请在搜索框输入您需要查询的用户..."
        return render(request,'user.html',{'notfound':notfound})