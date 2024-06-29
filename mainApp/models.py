from django.db import models

from usersApp.models import User


class Plan(models.Model):
    new = ('new', 'new')
    in_progress = ('in_progress', 'in_progress')
    done = ('done', 'done')

    status_choise = (new, in_progress, done)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    data_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=status_choise, default=new[0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'
