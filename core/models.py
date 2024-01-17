from django.db import models
    
class Regions(models.Model):
    region = models.CharField(max_length=25)
    image = models.ImageField(upload_to='upload/')
    background = models.ImageField(upload_to='upload/bg', blank=True)
    def __str__(self):
        return self.region;

class Record(models.Model):
    COLORS = [("#5eb1f5","record",),("#8321a3","guiness",),]
    def default_RecHold():
        return 'Рекордсмен'
    record_holder = models.CharField(max_length=100, default=default_RecHold)
    record_holders_age = models.IntegerField(blank=True, null=True)
    record_holders_city = models.CharField(max_length=100, blank=True)
    record_holders_region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    record_holder_image = models.ImageField(upload_to='upload/recordHolders', height_field=None, width_field=None, max_length=None, default='upload/recordHolders/default.png')
    record_info = models.CharField(max_length=1000, default="Інформація про рекорд відсутня")
    coordinate_y = models.FloatField(default=0.0)
    coordinate_x = models.FloatField(default=0.0)
    color = models.CharField(choices=COLORS, default='#5eb1f5', max_length=10)
    def __str__(self):
        i = 0
        if self.record_holder == 'Рекордсмен':
            i += 1
            return f'{self.record_holder} #{i}'
        else:
            return f'{self.record_holder}';
