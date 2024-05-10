from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Register_Method, User
from .serializers import UserSerializer
from google.oauth2 import id_token
from google.auth.transport import requests

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        print(serializer);
        if serializer.is_valid():
            # Get the register_method data from the request or any other source
            register_method_data = data.get('register_method')
            # Assuming register_method_data is the primary key of the Register_Method model
            register_method_instance = Register_Method.objects.get(pk=register_method_data)
            # Assign the register_method instance to the serializer's data
            serializer.validated_data['register_method'] = register_method_instance
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def get_session_variables(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    return JsonResponse({'user_id': user_id, 'username': username})

@csrf_exempt
def login_function(request):
    if request.method == 'POST':
        token = JSONParser().parse(request).get('credential')
        try:
            client_id = '775476638499-u0p0cb0rh659i1noniivn1oulqnd9urp.apps.googleusercontent.com'
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
            userid = idinfo['sub']

            user = User.objects.get(google_id=userid)
            return JsonResponse({'success': True, 'user_id': user.id, 'name': user.f_name})
        except User.DoesNotExist:
            # User does not exist
            return JsonResponse({'success': False, 'error': 'User not found'}, status=404)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid token'}, status=400)
