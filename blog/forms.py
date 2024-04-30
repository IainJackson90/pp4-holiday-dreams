from .models import Post, Comment
from django import forms
from crispy_forms.helper import FormHelper


class PostCreateForm(forms.ModelForm):
    """
    Customisation of form to create or update a post
    """
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'holiday_length', 'experience',
                  'bag_recommendation','cost_expected', 'featured_img',) #status



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'Comment',} 