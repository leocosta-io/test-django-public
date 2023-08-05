# Test Django

This is a small exam created to assess candidates to an internship role at Red Hat.

## Initial Information

### App overview

This is a simple app that registers instructors. On each instructor profile we have these fields:

- `name`
- `email`
- `username`
- `certid`
- `languages`
- `courses`

After start the Django server, you should be able see a list of instructors on: <http://localhost:8000/instructors/>

After you have finished all tasks you should be able to filter the list based on the language that instructors are able to speak:

- <http://localhost:8000/instructors/pt>: Should show only instructors that speak Portuguese
- <http://localhost:8000/instructors/es>: Should show only instructors that speak Spanish
- <http://localhost:8000/instructors/en>: Should show only instructors that speak English

The app is 95% ready, you need to finish all tasks in order have these features working properly.

### Setup

- requirement: python 3.x

- Django installation
If you don't have Django installed in your Python environment, you can run this command:

```bash
pip install -r requirements.txt
```

To check if you have Django installed you can use the command pip:

```bash
pip list
```

### Start the server

Inside the project directory, execute these steps:

```bash
cd latamtraining/
python manage.py runserver
```

After it, you should be able to access the project in your browser on <http://localhost:8000>

### Django Administration

After have the server running, you can access Django admin on <http://localhost:8000/admin>

```text
- Username: admin
- Password: redhat123
```

### Tests

The project provides 5 tests so you can ensure that you have finished the tasks correctly. The command bellow creates a `test database`, executes the tests and deletes the `test database`.

You can execute the tests with the command:

```bash
python manage.py test
```

When you have finished all tasks it should print something similar to this:

```text
$ python manage.py test 
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.042s

OK
Destroying test database for alias 'default'...
```

**You can execute these tests how many times you want.**

### Additional Information

There are 2 files that represent the final state of your database, when you have completed all tasks.

- `database_instructors.xlsx`: Each tab represents a table (or a Django Model).
- `test-django.jpg`: Diagram that represents the database final state. In blue, the Model Course, that you will have to create.

## Tasks

### Task 1: Create Model Course

On the file `latamtraining/instructors/models.py` create the fields for the Model `Course`:

- `name`: It will keep the course name, for example `Red Hat OpenShift I: Containers & Kubernetes`
- `sku`: It will keep the course code, for example `DO180`
- `page`: It will keep the URL for the course page, for example `https://www.redhat.com/en/services/training/do180-red-hat-openshift-I-containers-kubernetes`

**Ensure that this change was applied on database before proceed to other tasks.**

#### Task 1.1: (Not required but nice to have) Add Course Model on Django Admin

On the file `instructors/admin.py` configure Django Admin to show Course Model on <http://localhost:8000/admin>

### Task 2: Create fields `courses` inside `Instructor` Model

We need to register what courses an instructor is able to teach:

- create a new field on Instructor Model called `courses` using ManytoManyField and poiting to the new Model `Course` (created on the last task)

**Ensure that this change was applied on database before proceed to other tasks.**

### Task 3: Create a view to list instructors

On the file `latamtraining/instructors/views.py` insert the logic for the view ```list```:

- get instructors from database
- filter instructors based on the variable `language`
- if none language is passed the page lists all instructors

### Task 4: Show instructors name on `http://localhost:8000/instructors`

On the file `latamtraining/instructors/list.html` add the necessary code to show instructors name.
