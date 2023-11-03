from django.urls import path
from .views import (
    home,
    articles,
    all_html,
    # html_increment_likes,
    # decrease_likes
    subscribe,
    create_newsletter,
    subscription_successful
)
from . import views

# app_name = 'blog'

urlpatterns = [
    path("", home, name="home"),
    path("articles", articles, name="articles"),
    path("<int:id>", views.all_html, name="all_html"),
    path('subscription_successful/', views.subscription_successful, name="subscription_successful"),
    path('create/', views.create_newsletter, name="create_newsletter"),
    path('subscribe/<str:code>/', views.subscribe, name="subscribe"),
    path('send_verification_email/', views.send_verification_email, name="send_verification_email")
    # path("+1_like_html", html_increment_likes, name="html_increment_likes"),
    # path("-1_likes", decrease_likes, name="decrease_likes"),
]