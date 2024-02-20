from django.db import models

    

class Blogse(models.Model):
    img=models.ImageField( upload_to='photo')
    blog_name=models.CharField( max_length=50)
    title=models.CharField( max_length=50)
    discribtion=models.CharField( max_length=500)
    date=models.DateField()

    def __str__(self):
        return self.blog_name
