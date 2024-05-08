from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Register_Method, User
from .serializers import UserSerializer

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
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
