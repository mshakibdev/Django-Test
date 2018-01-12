from django.shortcuts import render
from DjangoApp.models import BlogPost
from datetime import datetime
from django.core.mail import send_mail
from DjangoApp.forms import ContactForm
from  django.http import HttpResponse


def index(request):

    posts = BlogPost.objects.all()

    if 'category' in request.GET:
        category = request.GET.get('category')
        posts = posts.filter(category=int(category))

    context = {
        'posts': posts.order_by('-time'),
        'datetime': datetime.now()
    }
    return render(request, 'index.html', context)


def view_post(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})


def get_info(request):
    if request.method == 'GET' or request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sub = form.cleaned_data['sub']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(sub, email, message, recipient_list= None)
            #return HttpResponse("<h1>Sent</h1>")
            return render(request, 'post.html', {'form': form})

    else:
        form = ContactForm()

    return render(request, 'post.html', {'form': form})

