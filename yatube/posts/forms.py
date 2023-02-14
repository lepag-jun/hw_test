from django.forms import ModelForm

from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        labels = {'group': 'Группа', 'text': 'Сообщение'}
        fields = ('text', 'group', 'image')
        help_texts = {
            'group': 'Группа, к которой будет относиться пост',
            'text': 'Введите текст поста',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {'text': 'Текст комментария'}
        help_texts = {'text': 'Hапишите ваш комментарий'}
