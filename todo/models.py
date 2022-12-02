from django.db import models

TASKSTATUS = (
    ('PENDING', 'Pending'),
    ('INPROCESS', 'Inprocess'),
    ('COMPLETE', 'Complete'),
)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    task_status = models.CharField(choices=TASKSTATUS, default= 'Pending', max_length=100)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name= 'todo', on_delete=models.CASCADE)


    def __str__(self):
        return self.title