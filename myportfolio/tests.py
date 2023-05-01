from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Permission
from django.urls import reverse

from myportfolio.initialize_models import *
from myportfolio.initialize_users_permissions import create_test_data_for_users_permissions


class MyPortfolioTests(TestCase):

    # All the test cases in this class have been conducted for superuser.

    def setUp(self):
        self.client = Client()
        self.superuser = get_user_model().objects.create_superuser(
            username='superuser_test',
            email='test@email.com',
            password='secret'
        )
        self.client.login(username='superuser_test', password='secret')

    def test_proficiency_unique_constraint(self):
        initialize_proficiency()
        proficiency = ProficiencyLevel(proficiency='Expert')
        with self.assertRaisesMessage(
                ValidationError,
                'ProficiencyLevel with this Proficiency already exists.'
        ):
            proficiency.full_clean()

    def test_school_unique_constraint(self):
        initialize_school()
        school = School(school='USC')
        with self.assertRaisesMessage(
                ValidationError,
                'School with this School already exists.'
        ):
            school.full_clean()

    def test_person_unique_constraint(self):
        initialize_person()
        person = Person(first_name='John', last_name='Shaw', phone_no='7789',
                          email_id='john@test.com', description='This is my description')
        with self.assertRaisesMessage(
                ValidationError,
                'Person with this First name, Last name and Disambiguator already exists.'
        ):
            person.full_clean()

    def test_person_list_view(self):
        initialize_person()
        response = self.client.get('/person/')
        no_response = self.client.get('/persons/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/person_list.html')
        self.assertContains(response, 'John Shaw')

    def test_person_detail_view(self):
        initialize_person()
        response = self.client.get('/person/1/')
        no_response = self.client.get('/person/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/person_detail.html')
        self.assertContains(response, 'John Shaw')

    def test_person_embedded_links(self):
        initialize_all()  # This function has sample data for all the classes
        response = self.client.get('/person/1/')

        # Check education hyperlink
        self.assertContains(response, '<a href="/education/1/"')
        embedded_education_link = self.client.get('/education/1/')
        self.assertEqual(embedded_education_link.status_code, 200)

        # Check experience hyperlink
        self.assertContains(response, '<a href="/experience/1/"')
        embedded_experience_link = self.client.get('/experience/1/')
        self.assertEqual(embedded_experience_link.status_code, 200)

        # Check project hyperlink
        self.assertContains(response, '<a href="/project/1/"')
        embedded_project_link = self.client.get('/project/1/')
        self.assertEqual(embedded_project_link.status_code, 200)

        # Check skill hyperlink
        self.assertContains(response, '<a href="/skill/1/"')
        embedded_skill_link = self.client.get('/skill/1/')
        self.assertEqual(embedded_skill_link.status_code, 200)

    def test_person_create_view(self):
        initialize_person()
        response = self.client.get('/person/create/')
        no_response = self.client.get('/persons/create/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/person_form.html')

    def test_person_update_view(self):
        initialize_person()
        response = self.client.get('/person/1/update/')
        no_response = self.client.get('/person/100/update/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/person_form_update.html')

    def test_person_delete_view(self):
        initialize_person()
        response = self.client.get('/person/1/delete/')
        no_response = self.client.get('/persons/100/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/person_confirm_delete.html')

    def test_education_unique_constraint(self):
        initialize_education()
        school = School.objects.get(school='UIUC')
        person = Person.objects.get(first_name='John', last_name='Shaw')
        education = Education(school=school, degree_name='MS',
                             start_date='2021-09-19', gpa='3.1', person_id=person)
        with self.assertRaisesMessage(
                ValidationError,
                'Education with this School, Degree name and Person id already exists.'
        ):
            education.full_clean()

    def test_education_list_view(self):
        initialize_education()
        response = self.client.get('/education/')
        no_response = self.client.get('/educations/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/education_list.html')
        self.assertContains(response, 'UIUC')

    def test_education_detail_view(self):
        initialize_education()
        response = self.client.get('/education/1/')
        no_response = self.client.get('/education/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/education_detail.html')
        self.assertContains(response, 'UIUC')

    def test_education_embedded_links(self):
        initialize_all()  # This function has sample data for all the classes
        response = self.client.get('/education/1/')

        # Check person hyperlink
        self.assertContains(response, '<a href="/person/1/"')
        embedded_person_link = self.client.get('/person/1/')
        self.assertEqual(embedded_person_link.status_code, 200)

    def test_education_create_view(self):
        initialize_education()
        response = self.client.get('/education/create/')
        no_response = self.client.get('/educations/create/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/education_form.html')

    def test_education_update_view(self):
        initialize_education()
        response = self.client.get('/education/1/update/')
        no_response = self.client.get('/education/100/update/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/education_form_update.html')

    def test_education_delete_view(self):
        initialize_education()
        response = self.client.get('/education/1/delete/')
        no_response = self.client.get('/education/100/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/education_confirm_delete.html')

    def test_experience_unique_constraint(self):
        initialize_experience()
        person = Person.objects.get(first_name='John', last_name='Shaw')
        experience = Experience(company_name='Bayer', job_title='Data Scientist',
                           start_date='2021-05-16', description='My description', person_id=person)
        with self.assertRaisesMessage(
                ValidationError,
                'Experience with this Company name, Start date and Person id already exists.'
        ):
            experience.full_clean()

    def test_experience_list_view(self):
        initialize_experience()
        response = self.client.get('/experience/')
        no_response = self.client.get('/experiences/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/experience_list.html')
        self.assertContains(response, 'Bayer')

    def test_experience_detail_view(self):
        initialize_experience()
        response = self.client.get('/experience/1/')
        no_response = self.client.get('/experience/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/experience_detail.html')
        self.assertContains(response, 'Bayer')

    def test_experience_embedded_links(self):
        initialize_all()  # This function has sample data for all the classes
        response = self.client.get('/experience/1/')

        # Check person hyperlink
        self.assertContains(response, '<a href="/person/1/"')
        embedded_person_link = self.client.get('/person/1/')
        self.assertEqual(embedded_person_link.status_code, 200)

    def test_experience_create_view(self):
        initialize_experience()
        response = self.client.get('/experience/create/')
        no_response = self.client.get('/experiences/create/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/experience_form.html')

    def test_experience_update_view(self):
        initialize_experience()
        response = self.client.get('/experience/1/update/')
        no_response = self.client.get('/experience/100/update/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/experience_form_update.html')

    def test_experience_delete_view(self):
        initialize_experience()
        response = self.client.get('/experience/1/delete/')
        no_response = self.client.get('/experience/100/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/experience_confirm_delete.html')

    def test_project_unique_constraint(self):
        initialize_project()
        person1 = Person.objects.get(first_name='John', last_name='Shaw')

        with self.assertRaises(Exception) as context:
            project = Project.objects.create(project_title='Test title', start_date='2021-05-16')
            project.persons.add(person1)

        self.assertTrue('UNIQUE' in str(context.exception))

    def test_project_list_view(self):
        initialize_project()
        response = self.client.get('/project/')
        no_response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/project_list.html')
        self.assertContains(response, 'Test title')

    def test_project_detail_view(self):
        initialize_project()
        response = self.client.get('/project/1/')
        no_response = self.client.get('/project/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/project_detail.html')
        self.assertContains(response, 'Test title')

    def test_project_embedded_links(self):
        initialize_all()  # This function has sample data for all the classes
        response = self.client.get('/project/1/')

        # Check person hyperlink
        self.assertContains(response, '<a href="/person/1/"')
        embedded_person_link = self.client.get('/person/1/')
        self.assertEqual(embedded_person_link.status_code, 200)

    def test_project_create_view(self):
        initialize_project()
        response = self.client.get('/project/create/')
        no_response = self.client.get('/projects/create/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/project_form.html')

    def test_project_update_view(self):
        initialize_project()
        response = self.client.get('/project/1/update/')
        no_response = self.client.get('/project/100/update/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/project_form_update.html')

    def test_project_delete_view(self):
        initialize_project()
        response = self.client.get('/project/1/delete/')
        no_response = self.client.get('/project/100/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/project_confirm_delete.html')

    def test_skill_unique_constraint(self):
        initialize_skill()
        person1 = Person.objects.get(first_name='John', last_name='Shaw')
        proficiency = ProficiencyLevel.objects.get(proficiency='Beginner')
        with self.assertRaises(Exception) as context:
            skill = Skill.objects.create(skill_name='Python', proficiency=proficiency)
            skill.persons.add(person1)

        self.assertTrue('UNIQUE' in str(context.exception))

    def test_skill_list_view(self):
        initialize_skill()
        response = self.client.get('/skill/')
        no_response = self.client.get('/skills/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/skill_list.html')
        self.assertContains(response, 'Python')

    def test_skill_detail_view(self):
        initialize_skill()
        response = self.client.get('/skill/1/')
        no_response = self.client.get('/skill/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/skill_detail.html')
        self.assertContains(response, 'Python')

    def test_skill_embedded_links(self):
        initialize_all()  # This function has sample data for all the classes
        response = self.client.get('/skill/1/')

        # Check person hyperlink
        self.assertContains(response, '<a href="/person/1/"')
        embedded_person_link = self.client.get('/person/1/')
        self.assertEqual(embedded_person_link.status_code, 200)

    def test_skill_create_view(self):
        initialize_skill()
        response = self.client.get('/skill/create/')
        no_response = self.client.get('/skills/create/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/skill_form.html')

    def test_skill_update_view(self):
        initialize_skill()
        response = self.client.get('/skill/1/update/')
        no_response = self.client.get('/skill/100/update/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/skill_form_update.html')

    def test_skill_delete_view(self):
        initialize_skill()
        response = self.client.get('/skill/1/delete/')
        no_response = self.client.get('/skill/100/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'myportfolio/base.html')
        self.assertTemplateUsed(response, 'myportfolio/skill_confirm_delete.html')

# Test cases for validating authorization and authentications:
# In 'myportfolio/initialize_users_permissions',
# I have created 3 user groups: test_group_user, test_group_clerk, test_group_operator which mimic the actual user
# groups portfolio_user, portfolio_clerk and portfolio_operator respectively


class TestUserPermissionsForUser(TestCase):

    # Testing permissions for user from the user group test_group_user

    def setUp(self):
        self.client = Client()
        initialize_all()
        create_test_data_for_users_permissions()

        # Credentials for the user from the user group test_group_user
        self.client.login(username='user1', password='{iSchoolUI}')

    def test_permission_user_list_view(self):
        response = self.client.get('/person/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/')
        self.assertEqual(response.status_code, 200)

    def test_permission_user_detail_view(self):
        response = self.client.get('/person/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/1/')
        self.assertEqual(response.status_code, 200)

    def test_permission_user_add_view(self):
        response = self.client.get('/person/create/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/education/create/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/experience/create/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/project/create/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/skill/create/')
        self.assertEqual(response.status_code, 403)

    def test_permission_user_change_view(self):
        response = self.client.get('/person/1/update/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/education/1/update/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/experience/1/update/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/project/1/update/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/skill/1/update/')
        self.assertEqual(response.status_code, 403)

    def test_permission_user_delete_view(self):
        response = self.client.get('/person/1/delete/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/education/1/delete/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/experience/1/delete/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/project/1/delete/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/skill/1/delete/')
        self.assertEqual(response.status_code, 403)

    def test_user_create_button(self):
        response = self.client.get('/person/')
        self.assertNotContains(response, 'Add new person')

    def test_user_edit_button(self):
        response = self.client.get('/person/1/')
        self.assertNotContains(response, 'Edit Person')

    def test_user_delete_button(self):
        response = self.client.get('/person/1/')
        self.assertNotContains(response, 'Delete Person')

class TestUserPermissionsForClerk(TestCase):
    # Testing permissions for user from the user group test_group_clerk

    def setUp(self):
        self.client = Client()
        initialize_all()
        create_test_data_for_users_permissions()

        # Credentials for the user from the user-group test_group_clerk
        self.client.login(username='clerk1', password='{iSchoolUI}')

    def test_permission_clerk_list_view(self):
        response = self.client.get('/person/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/')
        self.assertEqual(response.status_code, 200)

    def test_permission_clerk_detail_view(self):
        response = self.client.get('/person/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/1/')
        self.assertEqual(response.status_code, 200)

    def test_permission_clerk_add_view(self):
        response = self.client.get('/person/create/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/education/create/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/experience/create/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/project/create/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/skill/create/')
        self.assertEqual(response.status_code, 403)

    def test_permission_clerk_change_view(self):
        response = self.client.get('/person/1/update/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/education/1/update/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/experience/1/update/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/project/1/update/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/skill/1/update/')
        self.assertEqual(response.status_code, 403)

    def test_permission_clerk_delete_view(self):
        response = self.client.get('/person/1/delete/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/education/1/delete/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/experience/1/delete/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/project/1/delete/')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/skill/1/delete/')
        self.assertEqual(response.status_code, 403)

    def test_clerk_create_button(self):
        response = self.client.get('/person/')
        self.assertNotContains(response, 'Add new person')

    def test_clerk_edit_button(self):
        response = self.client.get('/person/1/')
        self.assertNotContains(response, 'Edit Person')

    def test_clerk_delete_button(self):
        response = self.client.get('/person/1/')
        self.assertNotContains(response, 'Delete Person')


class TestUserPermissionsForOperator(TestCase):

    # Testing permissions for user from the user group test_group_operator
    def setUp(self):
        self.client = Client()
        initialize_all()
        create_test_data_for_users_permissions()

        # Credentials for the user from the user-group test_group_operator
        self.client.login(username='operator1', password='{iSchoolUI}')

    def test_permission_operator_list_view(self):
        response = self.client.get('/person/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/')
        self.assertEqual(response.status_code, 200)

    def test_permission_operator_detail_view(self):
        response = self.client.get('/person/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/1/')
        self.assertEqual(response.status_code, 200)

    def test_permission_oeprator_add_view(self):
        response = self.client.get('/person/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/create/')
        self.assertEqual(response.status_code, 200)

    def test_permission_operator_change_view(self):
        response = self.client.get('/person/1/update/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/1/update/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/1/update/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/1/update/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/1/update/')
        self.assertEqual(response.status_code, 200)

    def test_permission_operator_delete_view(self):
        response = self.client.get('/person/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/education/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/experience/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/project/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/skill/1/delete/')
        self.assertEqual(response.status_code, 200)

    def test_operator_create_button(self):
        response = self.client.get('/person/')
        self.assertContains(response, 'Add new person')

    def test_operator_edit_button(self):
        response = self.client.get('/person/1/')
        self.assertContains(response, 'Edit Person')

    def test_operator_delete_button(self):
        response = self.client.get('/person/1/')
        self.assertContains(response, 'Delete Person')
