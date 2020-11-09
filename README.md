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
  
  