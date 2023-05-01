from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from myportfolio.forms import EducationForm, PersonForm, ExperienceForm, ProjectForm, SkillForm
from myportfolio.models import Person, Education, Experience, Project, Skill


class PersonList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Person
    permission_required = 'myportfolio.view_person'


class PersonDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Person
    permission_required = 'myportfolio.view_person'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        person = self.get_object()
        education_list = person.education.all()
        experience_list = person.experience.all()
        project_list = person.project_set.all()
        skill_list = person.skill_set.all()
        context['education_list'] = education_list
        context['experience_list'] = experience_list
        context['project_list'] = project_list
        context['skill_list'] = skill_list
        return context


class PersonCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PersonForm
    model = Person
    permission_required = 'myportfolio.add_person'


class PersonUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PersonForm
    model = Person
    template_name = 'myportfolio/person_form_update.html'
    permission_required = 'myportfolio.change_person'


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('myportfolio_person_list_urlpattern')
    permission_required = 'myportfolio.delete_person'

    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        education_list = person.education.all()
        experience_list = person.experience.all()
        project_list = person.project_set.all()
        skill_list = person.skill_set.all()
        if education_list.count() > 0 or experience_list.count() > 0 or project_list.count() > 0 or skill_list.count() > 0:
            return render(
                request,
                'myportfolio/person_refuse_delete.html',
                {'education_list': education_list,
                 'experience_list': experience_list,
                 'project_list': project_list,
                 'skill_list': skill_list
                 }
            )
        else:
            return render(
                request,
                'myportfolio/person_confirm_delete.html',
                {'person': person}
            )


class EducationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Education
    permission_required = 'myportfolio.view_education'


class EducationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Education
    permission_required = 'myportfolio.view_education'


class EducationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = EducationForm
    model = Education
    permission_required = 'myportfolio.add_education'


class EducationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = EducationForm
    model = Education
    template_name = 'myportfolio/education_form_update.html'
    permission_required = 'myportfolio.change_education'


class EducationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Education
    success_url = reverse_lazy('myportfolio_education_list_urlpattern')
    permission_required = 'myportfolio.delete_education'


class ExperienceList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Experience
    permission_required = 'myportfolio.view_experience'


class ExperienceDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Experience
    permission_required = 'myportfolio.view_experience'


class ExperienceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ExperienceForm
    model = Experience
    permission_required = 'myportfolio.add_experience'


class ExperienceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ExperienceForm
    model = Experience
    template_name = 'myportfolio/experience_form_update.html'
    permission_required = 'myportfolio.change_experience'


class ExperienceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Experience
    success_url = reverse_lazy('myportfolio_experience_list_urlpattern')
    permission_required = 'myportfolio.delete_experience'


class ProjectList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Project
    permission_required = 'myportfolio.view_project'


class ProjectDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Project
    permission_required = 'myportfolio.view_project'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        project = self.get_object()
        person_list = project.persons.all()
        context['person_list'] = person_list
        return context


class ProjectCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ProjectForm
    model = Project
    permission_required = 'myportfolio.add_project'


class ProjectUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ProjectForm
    model = Project
    template_name = 'myportfolio/project_form_update.html'
    permission_required = 'myportfolio.change_project'


class ProjectDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('myportfolio_project_list_urlpattern')
    permission_required = 'myportfolio.delete_project'


class SkillList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Skill
    permission_required = 'myportfolio.view_skill'


class SkillDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Skill
    permission_required = 'myportfolio.view_skill'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        skill = self.get_object()
        person_list = skill.persons.all()
        context['person_list'] = person_list
        return context


class SkillCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SkillForm
    model = Skill
    permission_required = 'myportfolio.add_skill'


class SkillUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SkillForm
    model = Skill
    template_name = 'myportfolio/skill_form_update.html'
    permission_required = 'myportfolio.change_skill'


class SkillDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Skill
    success_url = reverse_lazy('myportfolio_skill_list_urlpattern')
    permission_required = 'myportfolio.delete_skill'


