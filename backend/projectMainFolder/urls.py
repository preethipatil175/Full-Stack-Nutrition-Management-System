"""projectMainFolder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django_mongoengine.mongo_admin.sites import site
from user_details import models
from user_log import models
from recipes import models
from user_details.views import BmrTdeeAPIView,user_form
from user_log.views import UserLogView,UserLogDetailView
from recipes.views import AIRecipeView

# Register your MongoEngine model
# site.register(models.User_Details)

urlpatterns = [
    path('admin/', site.urls),
    path('user/',BmrTdeeAPIView.as_view()),
    path('user_form/',user_form),
    path('food-log',UserLogView.as_view()),
    path('food-log/<str:log_id>/',UserLogDetailView.as_view()),
    path('recipe/',AIRecipeView.as_view())
]

# urls.py
