# Switf Tests (Web)

This a two part application that aims to make the applications of exams quicker through web system and a tablet hybrid app.

## Do
- Install dependencies with:

```shell
  pip install -r requirements.txt
  npm install
```
- Then Run:

```shell
python manage.py migrate
python manage.py runserver
```

## Links
- **Django**
  - [Model Fields Reference](https://docs.djangoproject.com/en/1.8/topics/db/models/)
  - [Authentication Sytem](https://docs.djangoproject.com/en/1.8/topics/auth/default/)
- **Git**
  - [When .gitignore is not working](http://stackoverflow.com/questions/1139762/ignore-files-that-have-already-been-committed-to-a-git-repository)

## License
MIT

## Additional Info.
### If you need the user to be loged in to make user of a view
```python
@login_required(redirect_field_name='proximo')
```
### You can create a new permission in a model's Meta class
### For Example:
```python
class Task(models.Model):
    ...
    class Meta:
        permissions = (
            ("view_task", "Can see available tasks"),
        )
```
### You can you it in a view with:
```python
request.user.has_perm('task.view_task')
```
### Or you can use the decorator permission_required like so:
```python
permission_required('task.view_task')
```
