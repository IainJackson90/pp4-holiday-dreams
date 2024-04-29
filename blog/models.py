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
    # holiday_season = models.CharField(max_length=10, default='spring') #choices=SEASONS,  <----- Make it work dropdown
    holiday_length = models.CharField(max_length=200, blank=True)
    experience = models.TextField(blank=True)
    bag_recommendation =  models.TextField(max_length=200, blank=True)
    cost_expected = models.TextField(max_length=200, blank=True)
    featured_img = CloudinaryField('image', default='placeholder')
    # recommendation = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="blog_posts_recommendation"
    # )
    # content = models.TextField()  --> Recommendation
    # excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    # approved = models.BooleanField(default=False)
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



# class Recommendation(models.Model):
#     """
#     Stores a Recommendation of the holiday post entry related to :model:`blog.Post`.
#     """
#     # post = models.ForeignKey(Post, on_delete=models.CASCADE,
#     #                          related_name="comments")
#     # author = models.ForeignKey(
#     #     User, on_delete=models.CASCADE, related_name="commenter")
#     # destination = models.CharField(max_length=200)
#     recommendation = models.ForeignKey(
#         Post, on_delete=models.CASCADE, related_name="blog_posts_recommendation"
#     )
#     holiday_season = models.PositiveIntegerField(choices=SEASONS, default=1)
#     sites = models.CharField(max_length=200)
#     holiday_length = models.CharField(max_length=200)
#     # featured_image = CloudinaryField('image', default='placeholder')
#     restaurants = models.CharField(max_length=200)
#     to_avoid = models.CharField(max_length=200)
#     cost_expected = models.CharField(max_length=200)
#     bag_recommendation =  models.CharField(max_length=200)
#     # Maybe add a star rating in here ?
#     sites = models.TextField()
#     # approved = models.BooleanField(default=False)


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
    approved = models.BooleanField(default=False)  # Change this to comment without approval

    class Meta:
        ordering = ["-created_on"]
        #  ordering = ["-created_on", "author"]   # Maybe put this in the post model as well ?

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    
    
class Like(models.Model):
    """
    Stores a single like entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_Bool, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

