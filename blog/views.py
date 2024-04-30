from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Post, Comment, Like, User
from .forms import CommentForm, PostCreateForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    # queryset = Post.objects.all()
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 9


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_counter = post.comments.count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment was posted sucsefully'
                # Have to change this because their should be no approval
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
             "post": post,
             "comments": comments,
             "comment_counter": comment_counter,
             "comment_form": comment_form,
        },
)


# def recommendation_detail(request, slug, post_id, Post):
#     """
#     Display an individual :model:`blog.Post`.

#     **Context**

#     ``post``
#         An instance of :model:`blog.Post`.

#     **Template:**

#     :template:`blog/post_detail.html`
#     """
    
#     queryset = Recommendation.objects
#     # recommendation = get_object_or_404(queryset, slug=slug)
#     recommendation = get_object_or_404(Post, pk=post_id)
#     # recommendation = Recommendation

#     return render(
#         request,
#         "blog/post_detail.html",
#         {
#             "recommendation": recommendation
#         },
#     )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment was successfully updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class Like(View):
    """
    View for like on posts.
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Toggle like on posts.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreatePost(SuccessMessageMixin, CreateView):
    """
    View for creating a user post
    """
    model = Post
    template_name = "post_create.html"
    form_class = PostCreateForm
    success_url = reverse_lazy("home")
    success_message = "Your post has been shared success!"

    def form_valid(self, form):
        """
        Logged in user as author for post
        """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    
class PostUpdate(SuccessMessageMixin, UpdateView):
    """
    Updating a user post
    """
    model = Post
    form_class = PostCreateForm
    template_name = "update_post.html"
    success_message = "Your post has been updated successfully!"

    def get_queryset(self):
        """
        Override to get a queryset of the post.
        Only the author can update the post.
        """
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        """
        Takes user back to home page after the update was successful
        """
        return reverse('post_detail', kwargs={"slug": self.object.slug})
    
    
class DeletePost(SuccessMessageMixin, DeleteView):
    """
    Deleting an existing blog post created by a user
    """
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
    success_message = "Your post has been deleted successfully!"
    
    def test_func(self):
        """
        Validate that the current user is the author of the post being deleted
        """
        post = self.get_object()
        return self.request.user == post.author
