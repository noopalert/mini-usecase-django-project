from django.db import models
from django.utils.text import slugify

class DailyTrans(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateField(auto_now_add=True)
    modes = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    subcategories = models.CharField(max_length=100, null=True)
    amounts = models.IntegerField()
    types_transaction = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, editable=False)

    class Meta:
        db_table = 'dm_dailytrans'
        managed = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}. {} - {}'.format(self.id, self.categories,self.amounts)
    
