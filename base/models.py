from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from base.models import Bug
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField( max_length=500)
    content = RichTextField(blank=True,null=True)
    complete = models.BooleanField(default = False)
    #bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Bug(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    ticket = models.CharField( max_length=500)
    description = RichTextField(blank=True,null=True)
    status = models.BooleanField(default = False)  
    task = models.ForeignKey(Task, on_delete=models.CASCADE,null=True,blank=True)
    image =  models.ImageField( upload_to= 'base/images/',null=True,blank=True)
    attachment = models.FileField( upload_to='base/attachments/',null=True,blank=True)
    
    def __str__(self):
        return self.ticket

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.attachment.delete()
        super().delete(*args, **kwargs)

