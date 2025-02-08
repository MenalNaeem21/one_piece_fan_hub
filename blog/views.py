from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .models import Discussion, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login as django_login, logout as django_logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def login_view(request):
  
        form=AuthenticationForm(data=request.POST)   if request.method=='POST' else AuthenticationForm()
        if request.method=='POST' and form.is_valid():
            user=form.get_user()
            django_login(request,user)
            return redirect('home')
       
        return render(request, 'registration/login.html',{'form':form})

def logout_view(request):
    django_logout(request)
    return redirect('login')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            django_login(request,user)
            return redirect('discussion-list')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})



class discussionListView(ListView):
    model=Discussion
    template_name='blog/discussion_list.html'
    context_object_name = "discussions" #to acccess obj as discussions
    ordering=['-created_at'] #put latest post first

class discussionDetailView(DetailView):
    model=Discussion
    template_name='blog/discussion_detail.html'

class discussionCreateView(CreateView):
    model=Discussion
    fields=['title','content']
    template_name='blog/discussion_from.html'

    def form_valid(self, form):
        return super().form_valid(form)

@login_required    
def add_comment(request,discussion_id):
    discussion=get_object_or_404(Discussion,id=discussion_id)
    if request.method=="POST":
        content=request.POST["content"]
        Comment.objects.create(discussion=discussion,author=request.user,content=content)

    return redirect("discussion-detail",pk=discussion_id)