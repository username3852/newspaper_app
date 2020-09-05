from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reversee


class Article(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    count = models.IntegerField(default=0)
    # slug = models.SlugField(max_length=255, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True)  # it is needed only once
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="articles", null=True)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments',  # new
                                )
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("article_list")
