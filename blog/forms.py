from django import forms

from blog.models import Author_of_post, Post


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label='Заголовок')
    # description = forms.CharField(widget=forms.Textarea, label='Содержание поста')
    # is_published = forms.BooleanField(label='Активен')
    # # image = forms.ImageField(label='Изображение')
    author = forms.ModelChoiceField(queryset = Author_of_post.objects.all(), empty_label='Не выбран')
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'is_published', ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'description': forms.Textarea(attrs={'cols':50, 'rows':5})
        }
