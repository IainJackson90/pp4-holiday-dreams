from django.shortcuts import render
from .models import About
# Create your views here.


def about_blog(request):
    """
    A Page that will display a descriptive insight about what the
    blog is about and the goals of the site.
    
    **Template**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )