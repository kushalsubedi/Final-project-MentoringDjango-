from django.shortcuts import render
from .models import Post
from django.views import View

from .forms import CreatePost
# Create your views here.


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }
        return render(request, 'Home/index.html', context)

class PostDetailView(View):
    def get(self, request,id):
        post = Post.objects.get(id=id)
        context = {
            'post':post
        }
        return render(request, 'Home/post_detail.html', context)


class CreatePostView(View):
    def get(self, request):
        return render(request, 'Home/create_post.html')

    def post(self, request):
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.slug = form.title.replace(' ', '-')
            form.save()
        else :
            print (form.errors)
        return render(request, 'Home/create_post.html', {'form':form})
    
      
class UpdatePostView(View):
    def get(self, request,id):
        post = Post.objects.get(id=id)
        form = CreatePost(instance=post)
        return render(request, 'Home/create_post.html', {'form':form})

    def post(self, request, slug):
        post = Post.objects.get(id = id)
        form = CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.slug = form.title.replace(' ', '-')
            form.save()
        else :
            print (form.errors)
        return render(request, 'Home/create_post.html', {'form':form})

class DeletePostView(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        post.delete()
        return render(request, 'Home/index.html')
    

       
    
        