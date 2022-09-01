from django.urls import path

from .views import GraphQLPlaygroundView


app_name = 'graphql_api'


urlpatterns = [
    path(
        'playground/',
        GraphQLPlaygroundView.as_view(),
        name='playground',
    ),
]
