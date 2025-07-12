from django.db import models
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    last_updated = models.DateField(auto_now=True)
    current_version = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='game_covers/', blank=True, null=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('game_detail', args=[self.slug])

class MemoryOffset(models.Model):
    OFFSET_TYPES = [
        ('float', 'Float'),
        ('int', 'Integer'),
        ('byte', 'Byte'),
        ('bool', 'Boolean'),
        ('string', 'String'),
    ]
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='offsets')
    description = models.CharField(max_length=200)
    offset = models.CharField(max_length=50)
    offset_type = models.CharField(max_length=10, choices=OFFSET_TYPES)
    version = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.description} ({self.offset})"

class Pointer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='pointers')
    description = models.CharField(max_length=200)
    pointer_path = models.TextField()
    base_address = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.description} pointer"

class Trainer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='trainers')
    version = models.CharField(max_length=50)
    download_link = models.URLField(verbose_name="Trainer Download Link")
    download_link_ce_xml = models.URLField(
        verbose_name="Cheat Engine XML Download Link",
        blank=True,
        null=True,
        help_text="Optional link to download Cheat Engine XML table"
    )
    features = models.TextField()
    upload_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.game.title} Trainer v{self.version}"