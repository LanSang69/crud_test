from django.urls import path
from Users import views

urlpatterns = [
    path('Users/', views.user_list, name='user_list'),
    path('login/', views.handle_google_signin, name='handle_google_signin'),
]