from django.db import models

CATEGORY_CHOICES = (
    ('clothes', 'Clothes'),
    ('electronics', 'Electronics'),
    ('books', 'Books'),
    ('furniture', 'Furniture'),
    ('other', 'Other'),
)

class Donation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
