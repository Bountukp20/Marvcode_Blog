from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.mail import send_mail
from .forms import *
from django.utils.crypto import get_random_string

# Create your views here.

def home(request):
    visits = Visits.objects.all()
    
    for visits in visits:
        # if likes.like_num > 1:
            visits.num += 1
            visits.save()

    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            token = get_random_string(32)  # Generate a random verification token
            subscription = Subscriber(email=email, token=token)
            subscription.save()

            # Send a verification email
            subject = 'Verify your subscription for Marvcode-Blog'
            message = f'Click the following link to verify your subscription: {request.build_absolute_uri("/subscribe/" + token)}'
            from_email = 'marvcode.co@email.com'  # Replace with your email
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'blog/thank_you.html')
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


def subscribe(request, token):
    try:
        subscription = Subscriber.objects.get(token=token)
        subscription.verified = True
        subscription.save()
        return render(request, 'subscription_successful.html')
    except Subscriber.DoesNotExist:
        return render(request, 'blog/index.html')

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







