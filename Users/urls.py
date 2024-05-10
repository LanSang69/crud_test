from django.urls import path
from Users import views

urlpatterns = [
    path('Users/', views.user_list, name='user_list'),
    path('login/', views.login_function, name='login_function'),
    path('api/get-session-variables/', views.get_session_variables, name='get_session_variables'),
]