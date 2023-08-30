from django.urls import path
from .views import (
    home,
    articles,
    all_html
    # html_increment_likes,
    # decrease_likes
)
from . import views

# app_name = 'blog'

urlpatterns = [
    path("", home, name="home"),
    path("articles", articles, name="articles"),
    path("<int:id>", views.all_html, name="all_html"),
    # path("+1_like_html", html_increment_likes, name="html_increment_likes"),
    # path("-1_likes", decrease_likes, name="decrease_likes"),
]