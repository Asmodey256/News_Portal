from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Post


class PostForm(ModelForm):
    #check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'postCategory', 'title', 'text'
                  ]  # не забываем включить галочку в поля иначе она не будет показываться на странице!