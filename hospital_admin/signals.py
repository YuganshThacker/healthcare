from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver 
from hospital.models import User
from hospital_admin.models import Clinical_Laboratory_Technician
