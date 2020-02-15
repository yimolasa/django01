from django.db import models

# Create your models here.


class testtable(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

    def __str__(self):
        return "psql01 %s " % self.name
        

    class Meta:
        db_table = 'testtable01'
        app_label = 'psql01'
        
