from django.db import models

# Create your models here.
class Book(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    book_name = models.CharField(max_length=200)
    book_description 
    author
    publisher
    publish_date
    pages
    language
    file_size
    file_format
    url
    preview_text
    tags
    
class Author(models.Model):
    author_name
    
class Publisher(models.Model):
    publisher_name
    
class Tag(models.Model):Tag

class FileFormat(models.Model):Tag





    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'