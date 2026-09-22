from django.db import models
from datetime import datetime, date

class ShowManager(models.Manager):
    def basic_validator(self, post_data, show_id=None):
        errors = {}

        # 1.for the Title Validations
        title = post_data.get('title', '').strip()
        if len(title) < 2:
            errors['title'] = "Title should be at least 2 characters."
        
        # for the bonus: Uniqueness validation
        existing_shows = Show.objects.filter(title__iexact=title)
        if show_id:
            # Exclude the current show being updated
            existing_shows = existing_shows.exclude(id=show_id)
        if existing_shows.exists():
            errors['title_unique'] = "A show with this title already exists in the database."

        # 2. Network Validations
        network = post_data.get('network', '').strip()
        if len(network) < 3:
            errors['network'] = "Network should be at least 3 characters."

        # 3. Release Date Validations (this is NINJA BONUS)
        release_date_str = post_data.get('release_date', '').strip()
        if not release_date_str:
            errors['release_date'] = "Release Date is required."
        else:
            try:
                input_date = datetime.strptime(release_date_str, "%Y-%m-%d").date()
                if input_date >= date.today():
                    errors['release_date_past'] = "Release Date should be in the past."
            except ValueError:
                errors['release_date_invalid'] = "Invalid release date format."

        # 4. Description Validations (this is NINJA BONUS)
        description = post_data.get('description', '').strip()
        if description and len(description) < 10:
            errors['description'] = "Description is optional, but if present must be at least 10 characters."

        return errors



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()



def get_all_shows():
    return Show.objects.all()

def get_show_by_id(show_id):
    return Show.objects.get(id=show_id)

def create_show(data):
    return Show.objects.create(
        title=data['title'].strip(),
        network=data['network'].strip(),
        release_date=data['release_date'],
        description=data['description'].strip()
    )

def update_show(show_id, data):
    show = Show.objects.get(id=show_id)
    show.title = data['title'].strip()
    show.network = data['network'].strip()
    show.release_date = data['release_date']
    show.description = data['description'].strip()
    show.save()
    return show

def delete_show(show_id):
    show = Show.objects.get(id=show_id)
    show.delete()