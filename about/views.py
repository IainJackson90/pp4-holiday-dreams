from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import SubscribeForm
# Create your views here.


def about_blog(request):
    """
    A Page that will display a descriptive insight about what the
    blog is about and the goals of the site.
    
    **Template**
    :template:`about/about.html`
    """
    if request.method == "POST":
        subscribe_form = SubscribeForm(data=request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.add_message(request, messages.SUCCESS, "Subscribed successfully!")

    about = About.objects.all().order_by('-updated_on').first()
    subscribe_form = SubscribeForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "subscribe_form": subscribe_form},
    )