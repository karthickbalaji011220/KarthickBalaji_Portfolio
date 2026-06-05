from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    short_intro = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    career_objective = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    about_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=80)
    icon = models.CharField(max_length=100, blank=True, help_text='Font Awesome class or emoji')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.skill_name

    class Meta:
        ordering = ['order', 'skill_name']


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['order', '-year']


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role} at {self.company}"

    class Meta:
        ordering = ['order']


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField()
    full_description = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=500, help_text='Comma-separated technologies')
    project_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    features = models.TextField(blank=True, help_text='One feature per line')
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', '-created_at']

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]
