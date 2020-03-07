from products.models import Product
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    """
    A single Post
    """

    five_stars = '★★★★★'
    four_stars = '★★★★'
    three_stars = '★★★'
    two_stars = '★★'
    one_star = '★'
    RATING_CHOICES = (

        (five_stars, '5 Stars'),
        (four_stars, '4 Stars'),
        (three_stars, '3 Stars'),
        (two_stars, '2 Stars'),
        (one_star, '1 Star'),
        
    )

    product = models.ForeignKey(
        Product, related_name="products",
        on_delete=models.DO_NOTHING, default="")
    author = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.CharField(
        max_length=50, choices=RATING_CHOICES, default='five_stars')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="media", blank=True, null=True)

    def __str__(self):
        return self.title
