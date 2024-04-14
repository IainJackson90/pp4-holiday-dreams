from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
SEASONS = ((0, "Spring"), (1, "Summer"), (2, "Autumn"), (3, "Winter"))

# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    experience = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    # featured_img = CloudinaryField('image', default='placeholder')
    # recommendation = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="blog_posts_recommendation"
    # )
    # content = models.TextField()  --> Recommendation
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    # approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Posted by {self.author}"



class Recommendation(models.Model):
    """
    Stores a Recommendation of the holiday post entry related to :model:`blog.Post`.
    """
    # post = models.ForeignKey(Post, on_delete=models.CASCADE,
    #                          related_name="comments")
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="commenter")
    # destination = models.CharField(max_length=200)
    recommendation = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="blog_posts_recommendation"
    )
    holid_season = models.SlugField(choices=SEASONS, default=0)
    sites = models.CharField(max_length=200)
    holid_length = models.CharField(max_length=200)
    # featured_image = CloudinaryField('image', default='placeholder')
    restaurants = models.CharField(max_length=200)
    to_avoid = models.CharField(max_length=200)
    cost_expected = models.CharField(max_length=200)
    bag_recommendation =  models.CharField(max_length=200)
    # Maybe add a star rating in here ?
    over_view = models.TextField()
    # approved = models.BooleanField(default=False)
    
    
class Comment(models.Model):
    """
    Stores a single comment created by the user, to :model:`auth.User`
    and :model:`blog.Post`
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-created_on"]
        #  ordering = ["-created_on", "author"]             # Maybe put this in the most model aswell ?
        
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
