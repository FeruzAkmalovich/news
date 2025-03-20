from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Post,Category
from django.db.models import Q
from .forms import RegistrationForm
# Create your views here.


def index(request):
    post = Post.objects.all()
    category = Category.objects.all()
    popular = Post.objects.filter(popular__gte=10)
    return render(request,'index.html',{'post':post,'category':category,'popular':popular})


def post_detail(request,slug):
    posts = Post.objects.get(slug__iexact = slug)
    posts.popular+=1
    posts.save()
    return render(request,'post_detail.html',{'posts':posts})


def category_detail(request,slug):
    category = Category.objects.get(slug__iexact = slug)
    return render(request,'category_detail.html',{'category':category})



def search_result(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'search_obj':search_obj})



def register(request):
   
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})




def leave_comment(request,slug):
    try:
        posts = Post.objects.get(slug__iexact=slug)
    except:
        raise Http404('article page not found')
    
    if request.user.is_authenticated:
        user = request.user.username
        posts.comments.create(author_name=user,comment_text=request.POST.get('comment_text'))
    else:
        posts.comments.create(author_name=request.POST.get('author_name'),comment_text=request.POST.get('comment_text'))
    
    return HttpResponseRedirect(reverse('post_detail_url',args=(posts.slug,)))