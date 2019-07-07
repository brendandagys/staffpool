from django.db import models
from django.utils import timezone
# import datetime

# Create your models here.
class Messages(models.Model):
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Time of latest message')#, default=timezone.now())

    message_1 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 1', default='')
    message_2 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 2', default='')
    message_3 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 3', default='')
    message_4 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 4', default='')
    message_5 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 5', default='')
    message_6 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 6', default='')
    message_7 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 7', default='')
    message_8 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 8', default='')
    message_9 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 9', default='')
    message_10 = models.CharField(max_length=500, null=True, blank=True, verbose_name='Message 10', default='')

    author_1 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 1')
    author_2 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 2')
    author_3 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 3')
    author_4 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 4')
    author_5 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 5')
    author_6 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 6')
    author_7 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 7')
    author_8 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 8')
    author_9 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 9')
    author_10 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Author 10')

    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Messages'

    def __str__(self):
        # return self.code_red_status
        return 'Last 10 Messages Information'
