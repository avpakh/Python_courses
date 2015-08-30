from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class AgeManager(models.Manager):
    '''
    SImple manager that has methods to fetch old and young pets
    '''
    def get_young(self):
        '''
        Returns pets under 1 year or equal
        '''
        return super(AgeManager, self).get_queryset().filter(age__lte=1)

    def get_old(self):
        '''
        Returns pets older than 10 years
        '''
        return super(AgeManager, self).get_queryset().filter(age__gte=10)


class Pet(models.Model):
    """
    Model representing a pet
    """
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'))
    nickname = models.CharField("Nickname", max_length=100, blank=False, null=False)
    age = models.IntegerField("Age")
    sex = models.CharField("Sex", max_length=1, choices=SEX_CHOICES)

    ages = AgeManager()

    

    def get_full_info(self):
        return u'{0}:{1}:{2}'.format(self.nickname, self.age, self.sex)

    def save(self, *args, **kwargs):
        """
        Checks if Nickname starts with uppper
        """
        if self.nickname[0].islower():
            self.nickname.capitalize()
        super(Pet, self).save(*args, **kwargs)

    class Meta:
        ordering = ['nickname']
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

@receiver(pre_save, sender=Pet)
def my_callback(sender, instance, *args, **kwargs):
    if instance.age > 100:
        instance.age = 1
