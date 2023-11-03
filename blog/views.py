from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.mail import send_mail
from .forms import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import secrets
from django.urls import reverse
from django.http import JsonResponse

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

def generate_verification_code():
    return secrets.token_urlsafe(16)

def send_verification_email(email, code):
    verification_url = reverse('subscribe', args=[code])
    message = f"Click the following link to verify your subscription: {verification_url}"
    send_mail('Subscription Verification', message, 'your_email@example.com' [email])

def subscribe(request, code):
    # get_all_subs = Subscriber.objects.all()
    try:
        subscription = Subscriber.objects.get(verification_code=code)
        subscription.is_verified = True
        subscription.save()
        return redirect("subscription_successful")
    except Subscriber.DoesNotExist:
        return HttpResponse("Invalid email address")

def subscription_successful(request):
    return render(request, 'blog/subscription_successful.html')

def create_newsletter(request):
    # if user.is_superuser:
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()

            # Send the newsletter email to all subscribers
            subscribers = Subscriber.objects.all()
            subject = newsletter.subject
            content = newsletter.content
            sender_email = 'marvcode.co@gmail.com'

            for subscriber in subscribers:
                send_mail(
                    subject,
                    content,
                    sender_email,
                    [subscriber.email],
                    fail_silently=False,
                )

            return redirect('/')
    else:
        form = NewsletterForm()
    return render(request, 'blog/create_newsletter.html', {'form': form})
    # else:
    #     return redirect("/")

def custom_404(request, exception):
    return render(request, 'blog/404.html', status=404)







