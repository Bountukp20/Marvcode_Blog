from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')

def articles(request):
    HTML_Topics = Html.objects.all()
    Random_Topics = Random.objects.all()
    Css_Topics = Css.objects.all()
    JavaScript_Topics = JavaScript.objects.all()
    BootStrap_Topics = BootStrap.objects.all()
    Python_Topics = Python.objects.all()
    Django_Topics = Django.objects.all()
    React_Topics = React.objects.all()
    MySQL_Topics = MySQL.objects.all()
    ML_Topics = ML.objects.all()
    TypeScript_Topics = TypeScript.objects.all()
    
    context = {}
    context = {
        "Random_Topics": Random_Topics,
        "HTML_Topics": HTML_Topics,
        "Css_Topics": Css_Topics,
        "JavaScript_Topics": JavaScript_Topics,
        "BootStrap_Topics": BootStrap_Topics,
        "Python_Topics": Python_Topics,
        "Django_Topics": Django_Topics,
        "React_Topics": React_Topics,
        "MySQL_Topics": MySQL_Topics,
        "ML_Topics": ML_Topics,
        "TypeScript_Topics": TypeScript_Topics,
    }
    return render(request, 'blog/articles.html', context)
    
def all_html(request, id):
    HTML = get_object_or_404(Html, pk=id)
    # htmlLikes = HtmlLikes.objects.all()
    # LIKES = Html.objects.filter(id__in=HtmlLikes.id()).count()
    
    context = {}
    # context["htmlLikes"] = htmlLikes
    context["HTML"] = HTML
    # context = {
    #     'HTML': HTML,
    #     'sum_all_likes': sum_all_likes,
    # }
    
    return render(request, 'blog/all_html_topics.html', context)

# def html_increment_likes(request):
#     likes = Html.objects.all()
#     user_likes = HtmlLikes.objects.filter(user=request.user)

#     for likes in likes:
#         # if likes.like_num > 1:
#             likes.like_num += 1
#             likes.save()
    
#     for likes in user_likes:
#         # if likes.like_num > 1:
#             likes.like_num += 1
#             likes.save()
    
#     return redirect(request.META['HTTP_REFERER'])

# def decrease_likes(request):
#     likes = Html.objects.all()
#     user_likes = HtmlLikes.objects.filter(user=request.user)
    
#     for likes in likes:
#         # if likes.like_num > 1:
#             likes.like_num -= 1
#             likes.save()
    
#     for likes in user_likes:
#         # if likes.like_num > 1:
#             likes.like_num -= 1
#             likes.save()
    
#     return redirect(request.META['HTTP_REFERER'])













