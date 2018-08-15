from django.db import models

# Create your models here.


# ----------------------------------------------------------
class Partner(models.Model):
    name = models.CharField(max_length=45)
    link = models.URLField(max_length=250)
    image = models.ImageField(upload_to='uploads/partners/', max_length=45)

    def __str__(self):
        return self.name
# ----------------------------------------------------------
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=45, blank=False)
    email = models.EmailField(blank=False,default="someone@angoapp.com")
    photo = models.ImageField(upload_to="uploads/profiles/", max_length=45, blank=False)
    role = models.CharField(max_length=45, blank=True)
    administrator = models.BooleanField(default=False)
    bio = models.TextField(max_length=800, blank=True)
    linkedin = models.URLField(blank=False, default="https://linkedin/company/angoapp")
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Persons"

    # def get_slug(self):
    #     name = self.name.lower()
    #     name = name.replace(" ", "-")
    #     return name

    def __str__(self):
        return self.name
#----------------------------------------------------------

class Project(models.Model):
    title = models.CharField(max_length=30, blank=False)
    type = models.CharField(max_length=15, blank=False)
    manager = models.ForeignKey(Person)
    client = models.CharField(max_length=15, blank=False)
    description = models.TextField()
    link = models.CharField(max_length=300, blank=True)
    artwork = models.ImageField(upload_to='uploads/projects/', max_length=45, blank=True)
    featured = models.BooleanField(default=False)
    publishedDate = models.DateTimeField(auto_now=False)
    slug = models.SlugField(max_length=50, unique=True, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        verbose_name_plural = 'Portfolio Projects'

    def __str__(self):
        return self.title

    def uri(self):
        return reverse('project', args=[str(self.slug)])

    def get_author(self):
        return self.manager.name

#----------------------------------------------------------

# Similar to Color, Photo can be featured alongside Project.
# Multiple instances of Photo can also be created in the admin panel.
class Photo(models.Model):
    projectName = models.ForeignKey(Project)
    photo = models.ImageField(upload_to='uploads/projects/', max_length=45)

    def projectTitle(self):
        return self.projectName.title
#end Photo

#----------------------------------------------------------
