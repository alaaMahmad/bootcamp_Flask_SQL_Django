from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_all():
    return User.objects.all()
def add_new_user(data):
    User.objects.create(first_name=data["first_name"], last_name=data["last_name"], email_address=data["email"], age=data['age'])
