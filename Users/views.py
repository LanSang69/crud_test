from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import jwt
from .models import User
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
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def handle_google_signin(request):
  if request.method == 'POST':
    # Extract the credential from the request body
    try:
      credential = request.POST['credential']
    except KeyError:
      return JsonResponse({'error': 'Missing credential in request'}, status=400)

    # If successful, return a success message without the credential
    decoded = jwt.decode(credential, options={"verify_signature": False})
    return JsonResponse({'success': 'Login successful', 'crendentials': decoded}, status=200)

  else:
    # If the request method is not POST, return an error response
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)