from django.http import HttpResponse
from django.template import loader

from .models import Instructor, Language


def index(request):
    return HttpResponse(
        "Hello candidate!<br><br> Check the details for this test on <a href=https://github.com/leocosta-io/test-django/blob/main/README.md>https://github.com/leocosta-io/test-django/blob/main/README.md</a> or on the file README.md in your project."
    )


def list(request, language=None):
    template = loader.get_template("instructors/list.html")

    instructors = None

    ### Task 3: Get instructors from database and filter them based on the language

    ### Task 3 - End

    context = {
        "instructors": instructors,
    }
    return HttpResponse(template.render(context, request))
