from django import forms



class GameForm(forms.Form):
    selected_game = forms.ChoiceField(
        choices=[('coin', 'Coin'), ('cube', 'Cube'), ('number_random', 'Number_random')],
        required=False)
    quantity = forms.IntegerField(min_value=1, max_value=64)


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.Textarea
    author = forms.CharField(max_length=100)
    published = forms.BooleanField()