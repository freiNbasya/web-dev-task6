from django.shortcuts import render
from django.http import JsonResponse
import json
from .dummyEntries.users import users
from django.views.decorators.csrf import csrf_exempt

def user_list(request):
    context = {
        'users': users['users']
    }
    return render(request, 'user_list.html', context)

@csrf_exempt
def add_user(request):
    new_user = json.loads(request.body)
    users["users"].append(new_user)
    return JsonResponse({'message': 'User created successfully'}, status=201)

@csrf_exempt
def delete_user(request, name):
    if any(user['name'] == name for user in users['users']):
        users['users'] = [user for user in users['users'] if user['name'] != name]
        return JsonResponse({'message': f'User {name} deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': f'User {name} not found'}, status=404)
    
def user_profile(request, name):
    user = next((user for user in users['users'] if user['name'] == name), None)
    if user:
        return render(request, 'user_profile.html', {'user': user})
    else:
        return JsonResponse({'error': f'User {name} not found'}, status=404)
    
def image(request):
    return render(request, 'image.html')