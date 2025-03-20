from django.db import models
import string
import random

# Create your models here.
class ShortURL(models.Model):
    original_url = models.URLField(max_length=2000)
    short_code  = models.CharField(max_length=6, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    access_count = models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)
        
    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choice(characters) for _ in range(6))
            if not ShortURL.objects.filter(short_code=code).exists():
                return code
            
    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
    