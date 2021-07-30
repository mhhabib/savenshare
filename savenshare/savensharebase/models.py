from PIL import Image
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.


class LinkPost(models.Model):
    title = models.CharField("Set Link Title", max_length=200)
    weblink = models.CharField("Paste url", max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.title[:100]}...'

    def save(self):
        super().save()


"""
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
"""


class LinkWritePost(models.Model):
    posttitle = models.CharField("Set Post Title", max_length=200)
    description = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} -Post Name- {self.posttitle[:100]}...'

    def save(self):
        super().save()

    def get_absolute_url(self):
        return reverse('details', kwargs={'id': self.pk, 'author': self.author.username})


class LinkFile(models.Model):
    filetitle = models.CharField("Set File Title", max_length=200)
    uploadfile = models.FileField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} -File name- {self.filetitle[:100]}...'

    def save(self):
        super().save()
