from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(blank=True)
    created_datatime = models.DateTimeField(auto_now_add=True)
    updated_datatime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'メモ'
        verbose_name_plural = 'メモ'
    
    