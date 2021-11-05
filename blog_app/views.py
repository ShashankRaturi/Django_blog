from django.shortcuts import render , get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.models import User
from .models import Post

#from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>This is blog home.</h1>')


#dummy data:
# names = ["Aman" , "Shyaam" , "Raam" , "Reena"]

# posts = [
#     {
#         'author'      : 'Aman',
#         'title'       : 'Away from Home',
#         'content'     : 'First Post content',
#         'date_posted' : 'November 6 , 2018'
#     },
#     {
#         'author'      : 'Aviral',
#         'title'       : 'Homecoming',
#         'content'     : 'Fifth Post content',
#         'date_posted' : 'November 9 , 2019'
#     }
# ]

def home(request):
    context = {'posts' : Post.objects.all()}
    return render(request , 'blog_app/home.html' , context)


#class based view
class PostListView(ListView):
    model = Post  
    template_name = 'blog_app/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'  #this is our own name for the list as template variable
    ordering = ['-date_posted']
    paginate_by = 4



#to view all the posts of a particular user
class UserPostListView(ListView):
    model = Post  
    template_name = 'blog_app/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'  #this is our own name for the list as template variable
    paginate_by = 4

    #overriding
    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


#to view every post we can make use of detail view
class PostDetailView(DetailView):
    model = Post

    #<app>/<model>_<viewtype>.html

#to let the user create a post , we can use CreateView -> we dont even have to make any form to take input from user ,
#  it will take care of it.

class PostCreateView(LoginRequiredMixin , CreateView):  #with class based view we cannot use decorator , so instead we use mixin
    model = Post
    fields = ['title' , 'content']

    #<app>/<model>_form.html

    #overriding
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#to update the post at front end
class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):  #with class based view we cannot use decorator , so instead we use mixin
    model = Post
    fields = ['title' , 'content']

    #<app>/<model>_form.html

    #overriding
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #overriding
    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user:
            return True
        return False



class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Post
    success_url = '/'
    #overriding
    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user:
            return True
        return False

    #<app>/<model>_confirm_delete.html


def about(request):
    return render(request , 'blog_app/About.html' , {'title' : 'About'})
