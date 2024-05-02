from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
# SEASONS = (('spring', "Spring"), ('summer', "Summer"), ('autumn', "Autumn"), ('winter', "Winter"))
LIKE_Bool = (('Like', 'Like'),('Unlike', 'Unlike'))

# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    holiday_season = models.CharField(max_length=200, blank=True)
    holiday_length = models.CharField(max_length=200, blank=True)
    experience = models.TextField(blank=True)
    bag_recommendation =  models.TextField(max_length=200, blank=True)
    cost_expected = models.TextField(max_length=200, blank=True)
    featured_img = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User,
        related_name='post_likes',
        blank=True,
        )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Posted by {self.author}"
     
    def likes_count(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Stores a comment created by the user, to :model:`auth.User`
    and :model:`blog.Post`
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    
    
class Like(models.Model):
    """
    Stores a like related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_Bool, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

