from django.db import models


class Dataset(models.Model):
    dataset_name = models.CharField(max_length=200)
    dataset_file = models.FileField(upload_to='datasets/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dataset_name