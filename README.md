# learning_django_dev

The repository is used for my Django learning.

The instructions I'm following:

* [Django搭建个人博客, Dusai's Blog](https://www.dusaiphoto.com/article/2/)
* [Django documentation](https://docs.djangoproject.com/en/3.1/)

## Notes

> 2020-11-09

* Everytime modify `models.py`, remember `python manage.py makemigrations` and `python manage.py migrate`.

> 2020-11-10

* For Django 3.0, static configuration in `setting.py` needs to be:

  ```Python
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```
  
  instead of:
  
  ```Python
  STATICFILES_DIR = (
       os.path.join(BASE_DIR, 'static'),
  )
  ```
  

## Brief Conclusions

### Create a project

* Directory: `learning_django_dev`
  * Command: `django-admin startproject "project_name"`

### Create an APP

* Directory: `leaning_django_dev/zmei_django_dev`

  * Command: `python manage.py startapp "APP_name"`

* Directory: `leaning_django_dev/zmei_django_dev/zmei_django_dev`

  * `setting.py`

    add "APP_name" to `INSTALLED_APPS` list

  * `urls.py`

    import `include` from `django.urls`

    update `urlpatterns` list with

    ```python
    path('APP_name/', include('APP_name.urls', namespace='APP_name'))
    ```

* Directory: `leaning_django_dev/zmei_django_dev/zmei_django_dev/APP_name`

  * `urls.py`

    import `path` from `django.urls`

    `app_name = 'APP_name'`

    create blank list `urlpatterns`

### Modify `models.py`

* `APP_name/models.py` deal with the database

```python
from django.db import models
from django.contrib.auth.models import User
from django.utils import  timezone

# Create your models here.
class ArticlePost(models.Model):
		# example
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',) # order the articles by DESC created time
    
    def __str__(self):
        return self.title
```

> Reference: [Django搭建个人博客：编写博客文章的Model模型](https://www.dusaiphoto.com/article/11/)

* Remember run command `migrate`

