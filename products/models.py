from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):

    title = models.CharField(max_length=50)
    url = models.URLField()
    pub_date = models.DateField()
    votes_total = models.IntegerField(default=1)
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
