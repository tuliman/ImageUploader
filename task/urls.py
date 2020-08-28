from django.urls import path

from .views import ImageView, index, detail

urlpatterns = [
    path('', index,name='index'),
    path('<int:pk>/detail/', detail, name='detail'),
    path('test/', ImageView.as_view(), name='add_image'),
]
