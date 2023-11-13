from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
  #   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name ='home.html'
    ordering = ['-post_date']

class ArticleDetailView(DeleteView): 
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

    def form_valid(self, form):
        # Set updated_date only when the form is valid and the post is being updated
        if self.object.update_date:
            form.instance.update_date = None  # Clear updated_date to trigger save
        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')