from django import forms

from myportfolio.models import Education, Person, Experience, Project, Skill


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_dismbiguator(self):
        return self.cleaned_data['disambiguator'].strip()

    def clean_phone_no(self):
        return self.cleaned_data['phone_no'].strip()

    def clean_email_id(self):
        return self.cleaned_data['email_id'].strip()

    def clean_description(self):
        return self.cleaned_data['description'].strip()


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
            'start_date': DateInput(format=["%Y-%m-%d"], ),
            'end_date': DateInput(format=["%Y-%m-%d"], )
            }

    def clean_degree_name(self):
        return self.cleaned_data['degree_name'].strip()


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'start_date': DateInput(format=["%Y-%m-%d"], ),
            'end_date': DateInput(format=["%Y-%m-%d"], )
            }

    def clean_company_name(self):
        return self.cleaned_data['company_name'].strip()

    def clean_job_title(self):
        return self.cleaned_data['job_title'].strip()


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'start_date': DateInput(format=["%Y-%m-%d"], ),
            'end_date': DateInput(format=["%Y-%m-%d"], )
        }

    def clean_project_title(self):
        return self.cleaned_data['project_title'].strip()

    def clean_description(self):
        return self.cleaned_data['description'].strip()


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

    def clean_skill_name(self):
        return self.cleaned_data['skill_name'].strip()




