from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

#each class is like a table in database specifically in sql databases

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)

    #now we need author for our post but our user(author) is present in another table auth_user
    #here our user will have one-to-many relationship with  post as single user can have many posts
    #but one post can have only one user(author)


    #to do that we will use foreign key

    author = models.ForeignKey(User , on_delete = models.CASCADE , db_constraint=False) 
    #on_delete -> if user gets deleted then what we want to do with his/her posts , in this app we will delete them


    #now to update our database we will do migration


    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('post-detail' , kwargs = {'pk' : self.pk})
