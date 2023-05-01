from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class ProficiencyLevel(models.Model):
    proficiency_id = models.AutoField(primary_key=True)
    proficiency = models.CharField(max_length=40)

    def __str__(self):
        return '%s' % self.proficiency

    class Meta:
        verbose_name = "ProficiencyLevel"
        verbose_name_plural = "ProficiencyLevel"

        constraints = [
            UniqueConstraint(fields=['proficiency'], name='unique_proficiency')
        ]


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.school

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

        constraints = [
            UniqueConstraint(fields=['school'], name='unique_schools')
        ]


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    disambiguator = models.CharField(max_length=50, blank=True, default='')
    phone_no = models.CharField(max_length=15)
    email_id = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s %s' % (self.first_name, self.last_name)
        else:
            result = '%s %s (%s)' % (self.first_name, self.last_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('myportfolio_person_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('myportfolio_person_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('myportfolio_person_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

        constraints = [
            UniqueConstraint(fields=['first_name', 'last_name', 'disambiguator'], name='unique_person')
        ]


class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, related_name='schools', on_delete=models.PROTECT)
    degree_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    gpa = models.CharField(max_length=10)
    person_id = models.ForeignKey(Person, related_name='education', on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % self.school

    def get_absolute_url(self):
        return reverse('myportfolio_education_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('myportfolio_education_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('myportfolio_education_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

        constraints = [
            UniqueConstraint(fields=['school', 'degree_name', 'person_id'], name='unique_school')
        ]


class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    person_id = models.ForeignKey(Person, related_name='experience', on_delete=models.PROTECT)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('myportfolio_experience_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('myportfolio_experience_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('myportfolio_experience_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

        constraints = [
            UniqueConstraint(fields=['company_name', 'start_date', 'person_id'], name='unique_company')
        ]


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    persons = models.ManyToManyField('Person')
    description = models.TextField()

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse('myportfolio_project_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('myportfolio_project_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('myportfolio_project_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

        constraints = [
            UniqueConstraint(fields=['project_title'], name='unique_project')
        ]


class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    proficiency = models.ForeignKey(ProficiencyLevel, related_name='skills', on_delete=models.PROTECT)
    persons = models.ManyToManyField('Person')

    def __str__(self):
        return '%s - %s' % (self.skill_name, self.proficiency)

    def get_absolute_url(self):
        return reverse('myportfolio_skill_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('myportfolio_skill_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('myportfolio_skill_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

        ordering = ['skill_name']
        constraints = [
            UniqueConstraint(fields=['skill_name', 'proficiency'], name='unique_skill')
        ]


