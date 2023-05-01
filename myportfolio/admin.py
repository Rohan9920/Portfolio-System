from django.contrib import admin
from .models import (
    ProficiencyLevel,
    Person,
    Education,
    Experience,
    Project,
    Skill,
    School,
)


admin.site.register(ProficiencyLevel)
admin.site.register(Person)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(School)


