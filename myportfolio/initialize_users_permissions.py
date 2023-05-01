from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from myportfolio.models import Person, Education, Experience, Project, Skill


def create_test_data_for_users_permissions():

    # Created 3 user groups: test_group_user, test_group_clerk, test_group_operator which mimic the
    # actual user groups portfolio_user, portfolio_clerk and portfolio_operator respectively

    content_type = ContentType.objects.get_for_model(Person)
    person_view = Permission.objects.get(content_type=content_type, codename='view_person')
    person_add = Permission.objects.get(content_type=content_type, codename='add_person')
    person_change = Permission.objects.get(content_type=content_type, codename='change_person')
    person_delete = Permission.objects.get(content_type=content_type, codename='delete_person')

    content_type = ContentType.objects.get_for_model(Education)
    education_view = Permission.objects.get(content_type=content_type, codename='view_education')
    education_add = Permission.objects.get(content_type=content_type, codename='add_education')
    education_change = Permission.objects.get(content_type=content_type, codename='change_education')
    education_delete = Permission.objects.get(content_type=content_type, codename='delete_education')

    content_type = ContentType.objects.get_for_model(Experience)
    experience_view = Permission.objects.get(content_type=content_type, codename='view_experience')
    experience_add = Permission.objects.get(content_type=content_type, codename='add_experience')
    experience_change = Permission.objects.get(content_type=content_type, codename='change_experience')
    experience_delete = Permission.objects.get(content_type=content_type, codename='delete_experience')

    content_type = ContentType.objects.get_for_model(Project)
    project_view = Permission.objects.get(content_type=content_type, codename='view_project')
    project_add = Permission.objects.get(content_type=content_type, codename='add_project')
    project_change = Permission.objects.get(content_type=content_type, codename='change_project')
    project_delete = Permission.objects.get(content_type=content_type, codename='delete_project')

    content_type = ContentType.objects.get_for_model(Skill)
    skill_view = Permission.objects.get(content_type=content_type, codename='view_skill')
    skill_add = Permission.objects.get(content_type=content_type, codename='add_skill')
    skill_change = Permission.objects.get(content_type=content_type, codename='change_skill')
    skill_delete = Permission.objects.get(content_type=content_type, codename='delete_skill')

    # Giving permissions to test_group_user similar to the group portfolio_user
    test_group_user = Group.objects.create(name='Test Group User')
    test_group_user.permissions.add(person_view, education_view, experience_view, project_view, skill_view)
    user1 = User.objects.create_user(username='user1', password='{iSchoolUI}')
    user2 = User.objects.create_user(username='user2', password='{iSchoolUI}')
    test_group_user.user_set.add(user1, user2)

    # Giving permissions to test_group_clerk similar to the group portfolio_clerk
    test_group_clerk = Group.objects.create(name='Test Group Clerk')
    test_group_clerk.permissions.add(person_view, education_view, experience_view, project_view, skill_view)
    clerk1 = User.objects.create_user(username='clerk1', password='{iSchoolUI}')
    clerk2 = User.objects.create_user(username='clerk2', password='{iSchoolUI}')
    test_group_clerk.user_set.add(clerk1, clerk2)

    # Giving permissions to test_group_operator similar to the group portfolio_operator
    test_group_operator = Group.objects.create(name='Test Group Operator')
    test_group_operator.permissions.add(person_view, education_view, experience_view, project_view, skill_view,
                                        person_add, education_add, experience_add, project_add, skill_add,
                                        person_change, education_change, experience_change, project_change, skill_change,
                                        person_delete, education_delete, experience_delete, project_delete, skill_delete)
    operator1 = User.objects.create_user(username='operator1', password='{iSchoolUI}')
    operator2 = User.objects.create_user(username='operator2', password='{iSchoolUI}')
    test_group_operator.user_set.add(operator1, operator2)


