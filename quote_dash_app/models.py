from django.db import models

# Create your models here.
import re

class UserManager(models.Manager):
    def reg_validator(self,postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 3 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters" 
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords do not match!"
        return errors

    def login_validator(self,postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['login_email']):
            errors['login'] = "Invalid email and/or password"
        if len(postData['login_password']) < 8:
            errors['login'] = "Invalid email and/or password"
        return errors
    
    def edit_validator(self,postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['edit_email']):
            errors['edit_email'] = "Invalid email"
        if len(postData['edit_first_name']) < 2:
            errors['edit_first_name'] = "First name must be at least 3 characters"
        if len(postData['edit_last_name']) < 2:
            errors['edit_last_name'] = "Last name must be at least 3 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class QuoteManager(models.Manager):
    def quote_validator(self,postData):
        errors={}
        if len(postData['author']) < 3:
            errors['author'] = "Author must be more than 3 characters"
        if len(postData['quote']) < 10:
            errors['quote'] = "Quote must be more than 10 characters"
        return errors

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    user = models.ForeignKey(User,related_name="quotes",on_delete = models.CASCADE)
    likes = models.ManyToManyField(User,related_name="liked_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()