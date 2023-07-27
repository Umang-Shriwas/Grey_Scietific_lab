from django.db import models
from accounts.models import *

class PatientRecords(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.TextField()
    observations = models.TextField()
    treatments = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    misc = models.TextField()
    
   

    def __str__(self):
        return f"Record ID: {self.record_id}, Patient: {self.patient_id.name}"
    




