from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView, ListView

from blog.forms import AddPostForm
from blog.models import Post, Author_of_post


# def get_list(request):
#     return render(request, 'main.html', {'post_list': Post.objects.all()})


class ListPost(ListView):
    template_name = 'main.html'
    # context_object_name = 'posts'
    title_page = "asssssd"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all()

@login_required
def get_author(requests):
    return render(requests, 'author.html', {'title': 'ffff', 'author_list': Author_of_post.objects.all()})

class AuthorPost(ListView):
    template_name = 'author.html'

    def get_queryset(self):
        return Author_of_post.objects.all()

class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'add.html'
    # title_page = "vvvvvvv"
    extra_context = {

        'title': "Добавить статью"
    }




# def add_post(requests):
#     if requests.method == 'POST':
#         form = AddPostForm(requests.POST)
#         if form.is_valid():
#             Post.objects.create(**form.cleaned_data)
#
#             # print(form.cleaned_data)
#     else:
#         form = AddPostForm()
#
#     data = {
#         'title': 'Добавить пост',
#         'form': form
#     }
#     return render(requests, 'add.html', data)