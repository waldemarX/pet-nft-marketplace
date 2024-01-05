from django.urls import path

from . import views

app_name = 'profiling'

urlpatterns = [
    path('<slug:author_slug>', views.profile, name='profile'),
    path('collection/<slug:collection_slug>', views.collection, name='collection'),
    path('item/<int:id>', views.item, name='item')
]
