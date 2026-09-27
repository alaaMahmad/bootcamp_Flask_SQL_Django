from django.db import models
import re
from datetime import datetime, date

# --- MANAGERS & VALIDATORS ---

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if not postData.get('username') or not postData.get('first_name') or not postData.get('last_name') or not postData.get('email') or not postData.get('password'):
            errors["required"] = "All fields are required."
        
        if len(postData.get('first_name', '')) < 4:
            errors["first_name"] = "First name should be at least 4 characters."
            
        if len(postData.get('last_name', '')) < 4:
            errors["last_name"] = "Last name should be at least 4 characters."
            
        if not EMAIL_REGEX.match(postData.get('email', '')):
            errors["email"] = "Email must be a valid email."
            
        if User.objects.filter(username=postData.get('username')).exists():
            errors["username_exists"] = "Account username already exists."

        if User.objects.filter(email=postData.get('email')).exists():
            errors["email_exists"] = "Account email already exists."
            
        if len(postData.get('password', '')) < 8:
            errors["password_len"] = "Password minimum 8 characters."
            
        if postData.get('password') != postData.get('confirm_pw'):
            errors["pw_match"] = "PW and Confirm PW must match."
            
        return errors

class ParticipantManager(models.Manager):
    def participant_validator(self, postData):
        errors = {}
        
        first_name = postData.get('first_name', '').strip()
        last_name = postData.get('last_name', '').strip()
        phone_number = postData.get('phone_number', '').strip()
        start_date_str = postData.get('start_date', '')
        end_date_str = postData.get('end_date', '')

        if not all([first_name, last_name, phone_number, start_date_str, end_date_str]):
            errors["required"] = "All fields are required."

        if len(first_name) < 7:
            errors["first_name"] = "First name min 7 characters."

        if len(last_name) < 7:
            errors["last_name"] = "Last name min 7 characters."

        if len(phone_number) != 10 or not phone_number.isdigit():
            errors["phone_number"] = "Phone number must be 10 chars only."

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            today = date.today()

            if start_date >= today:
                errors["start_date"] = "Start date should be in the past."

            if end_date <= today:
                errors["end_date"] = "End date must be in the future."

        return errors

# --- DATABASE MODELS ---

class User(models.Model):
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Participant(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, related_name="participants", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ParticipantManager()


# --- DATABASE HELPER FUNCTIONS (ENCAPSULATED DATA ACCESS) ---

def add_user(data, pw_hash):
    return User.objects.create(
        username=data['username'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone_number=data.get('phone_number', ''),
        password=pw_hash
    )

def get_user_by_username(username):
    users = User.objects.filter(username=username)
    return users[0] if users else None

def get_user_by_id(user_id):
    return User.objects.get(id=user_id)

def add_participant(data, user_id):
    user = get_user_by_id(user_id)
    return Participant.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        phone_number=data['phone_number'],
        email=user.email,
        start_date=data['start_date'],
        end_date=data['end_date'],
        created_by=user
    )

def get_all_participants():
    return Participant.objects.all()

def get_participant_by_id(participant_id):
    return Participant.objects.get(id=participant_id)

def update_participant(participant_id, data):
    participant = Participant.objects.get(id=participant_id)
    participant.first_name = data['first_name']
    participant.last_name = data['last_name']
    participant.email = data.get('email', participant.email)
    participant.phone_number = data['phone_number']
    participant.start_date = data['start_date']
    participant.end_date = data['end_date']
    participant.save()
    return participant

def delete_participant(participant_id, user_id):
    participant = Participant.objects.get(id=participant_id)
    if participant.created_by.id == user_id:
        participant.delete()

def get_active_participants():
    today = date.today()
    return Participant.objects.filter(start_date__lte=today, end_date__gte=today)