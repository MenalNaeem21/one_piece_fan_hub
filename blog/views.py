from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Discussion
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

class discussionListView(ListView):
    model=Discussion
    template_name='blog/discussion_list.html'
    context_object_name = "discussions" #to acccess obj as discussions
    ordering=['-created_'] #put latest post first

class discussionDetailView(DetailView):
    model=Discussion
    template_name='blog/discussion_list.html'

class discussionCreateView(CreateView):
    model=Discussion
    fields=['title','content']
    template_name='blog/discussion_from.html'

    def form_valid(self, form):
        return super().form_valid(form)