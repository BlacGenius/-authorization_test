
from django.urls import path, include

from mainapp.views import (RegisterView,
                           UserView,
                           TokenView)



urlpatterns = [

    path('register/', RegisterView.as_view()),
    path('user/token/<int:pk>/', TokenView.as_view()),
    path('user/', UserView.as_view({'get': 'list'})),
    path('user/auth/', include('rest_framework.urls'))
]