"""twitter_django_api URL Configuration

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

import os

from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'graphql/',
        csrf_exempt(
            GraphQLView.as_view(
                graphiql=os.environ.get(
                    'TWITTER_CLONE_API_ENABLE_GRAPHIQL', False
                ),
            ),
        ),
        name='graphql',
    ),
    path('graphql_api/', include('graphql_api.urls')),
]
