from django.db import models

# Create your models here.
class BasicInfo(models.Model):
    address_text = models.CharField(max_length = 200)
    code_text = models.CharField(max_length = 10)
    schoolname_text = models.CharField(max_length = 200)
    location_text = models.CharField(max_length = 200)
    contact_text= models.CharField(max_length = 200)
    tel_text= models.CharField(max_length = 200)
    email_text= models.CharField(max_length = 200)
    grade_text= models.CharField(max_length = 200)
    teachersnum_text= models.CharField(max_length = 200)
    studentnum_text= models.CharField(max_length = 200)
    fill_date = models.CharField(max_length = 200)

    def __str__(self):
        return self.address_text
    
