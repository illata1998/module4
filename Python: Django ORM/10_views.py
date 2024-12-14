from django.db.models import Count, Prefetch
from django.shortcuts import render
from django_app.models import Teacher, Course


def index(request):
    # BEGIN
    courses_with_students = Prefetch('courses', queryset=Course.objects.prefetch_related('students'))  # noqa: E501
    teachers = Teacher.objects \
        .prefetch_related(courses_with_students) \
        .annotate(total_students=Count('courses__students', distinct=True))

    return render(request, 'index.html', {
        'teachers': teachers,
        })
    # END
