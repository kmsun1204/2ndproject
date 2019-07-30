
from django.contrib import admin
from django.urls import path
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('story/', blog.views.story, name="story"),
    path('messages/', blog.views.messages, name="messages"),
    path('blog/<int:blog_id>/', blog.views.detail, name='detail'),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create/', blog.views.create, name='create'),
]
