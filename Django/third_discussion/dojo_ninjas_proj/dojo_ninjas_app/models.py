from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="old dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_all_dojos():
    return Dojo.objects.all()

def create_dojo(data):
    Dojo.objects.create(name=data['name'],city=data['city'],state=data['state'])
def create_ninja(data):
    dojo_id = data['dojo_id']
    selected_dojo = Dojo.objects.get(id=dojo_id)
    Ninja.objects.create(first_name=data['first_name'],last_name=data['last_name'],dojo=selected_dojo)
    
def delete_dojo(dojo_id):
    dojo_to_delete = Dojo.objects.get(id=dojo_id)
    dojo_to_delete.delete()