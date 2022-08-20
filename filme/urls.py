# 3(coisas que precisa criar) => url - view - - template


from django.urls import path, include
from .views import homepage


urlpatterns = [
    path('', homepage),
]