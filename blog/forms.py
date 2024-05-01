from .models import Post, Comment
from django import forms
from crispy_forms.helper import FormHelper
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostCreateForm(forms.ModelForm):
    """
    Customisation of form to create or update a post
    """
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'holiday_season', 'holiday_length', 'experience',
                  'bag_recommendation','cost_expected', 'featured_img',) #status
        
        widgets = {
            "experience": SummernoteWidget(attrs={"class": "form-control"}),
            "bag_recommendation": SummernoteWidget(attrs={"class": "form-control"}),
            "cost_expected": SummernoteWidget(attrs={"class": "form-control"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'Comment',}
        
