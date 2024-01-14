from django.db import models

# Create your models here.
class Setting(models.Model):
    top_bg = models.FileField(
        upload_to="bg/"
    )
    footer_bg = models.FileField(
        upload_to="bg/"
    )
    email_bg = models.FileField(
        upload_to="bg/"
    )
    gallery_bg = models.FileField(
        upload_to='bg/'
    )
    trips = models.CharField(
        max_length=25
    )
    tourists = models.CharField(
        max_length=25
    )
    gallery_vid1 = models.FileField(
        upload_to="gallery/"
    )
    gallery_vid2 = models.FileField(
        upload_to="gallery/"
    )
    gallery_vid3 = models.FileField(
        upload_to="gallery/"
    )
    
    def __str__(self):
        return f"Настройки сайта {self.id}"
    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'
class Tours(models.Model):
    title = models.CharField(
        max_length=2555
    )
    price = models.CharField(
        max_length=2555
    )
    days = models.CharField(
        max_length=2555
    )
    bg_image = models.ImageField(
        upload_to='bg/'
    )
    price1 = models.CharField(
        "Цена на 1 человека",
        max_length=25
    )
    price2 = models.CharField(
        "Цена на 2 человека",
        max_length=25
    )
    price3 = models.CharField(
        "Цена на 3 человека",
        max_length=25
    )
    price4 = models.CharField(
        "Цена на 4 человека",
        max_length=25
    )
    included = models.CharField(
        max_length=255
    )
    not_included = models.CharField(
        max_length=255
    )
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
class Days(models.Model):
    title = models.CharField(
        max_length=150
    )
    image = models.ImageField(
        upload_to='tour_image/'
    )
    title_desc = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=555
    )
    tour = models.ForeignKey(
        Tours,
        related_name="tour_days",
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'День тура'
        verbose_name_plural = 'Дни туров'
class Video(models.Model):
    video = models.FileField(
        upload_to='gallery'
    )
    def __str__(self):
        return f"Видео {self.id}"
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео галлерея'
class Photo(models.Model):
    photo = models.ImageField(
        upload_to='gallery/'
    )
    def __str__(self):
        return f"Фото {self.id}"    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото галлерея'
