from django.db import models


class CycleInGraphError(Exception):
    "An exception that means that some graph has cycles."


class Task(models.Model):
    value = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    @property
    def root(self):
        "Returns a root task (task which parent is None)."
        # BEGIN
        seen_tasks = set()

        def walk(task):
            if not task.parent_id:
                return task
            elif task.id in seen_tasks:
                raise CycleInGraphError(task.id)
            seen_tasks.add(task.id)
            return walk(task.parent)

        return walk(self)
        # END
