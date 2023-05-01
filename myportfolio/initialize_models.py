
from myportfolio.models import (
    ProficiencyLevel,
    School,
    Person,
    Education,
    Experience,
    Project,
    Skill
)


def initialize_proficiency():
    ProficiencyLevel.objects.create(proficiency='Beginner')
    ProficiencyLevel.objects.create(proficiency='Intermediate')
    ProficiencyLevel.objects.create(proficiency='Expert')


def initialize_school():
    School.objects.create(school='UIUC')
    School.objects.create(school='NCSU')
    School.objects.create(school='USC')


def initialize_person():
    Person.objects.create(first_name='John', last_name='Shaw', phone_no='1234',
                          email_id='john@test.com', description='This is my description')
    Person.objects.create(first_name='Adam', last_name='Foden', phone_no='5678',
                          email_id='adam@test.com', description='This is my description too')

def initialize_education():
    person1 = Person.objects.create(first_name='John', last_name='Shaw', phone_no='1234',
                          email_id='john@test.com', description='This is my description')
    school1 = School.objects.create(school='UIUC')
    Education.objects.create(school=school1, degree_name='MS',
                             start_date='2021-08-19', gpa='4', person_id=person1)

def initialize_experience():
    person1 = Person.objects.create(first_name='John', last_name='Shaw', phone_no='1234',
                                    email_id='john@test.com', description='This is my description')
    Experience.objects.create(company_name='Bayer', job_title='Intern',
                           start_date='2021-05-16', description='My description', person_id=person1)


def initialize_project():
    person1 = Person.objects.create(first_name='John', last_name='Shaw', phone_no='1234',
                                    email_id='john@test.com', description='This is my description')
    person2 = Person.objects.create(first_name='Peter', last_name='Drury', phone_no='5678',
                                    email_id='peter@test.com', description='This is my description')
    project = Project.objects.create(project_title='Test title', start_date='2021-05-16')
    project.persons.add(person1, person2)


def initialize_skill():
    proficiency = ProficiencyLevel.objects.create(proficiency='Beginner')
    person1 = Person.objects.create(first_name='John', last_name='Shaw', phone_no='1234',
                                    email_id='john@test.com', description='This is my description')
    person2 = Person.objects.create(first_name='Peter', last_name='Drury', phone_no='5678',
                                    email_id='peter@test.com', description='This is my description')
    skill = Skill.objects.create(skill_name='Python', proficiency=proficiency)
    skill.persons.add(person1, person2)

def initialize_all():
    proficiency = ProficiencyLevel.objects.create(proficiency='Beginner')
    person1 = Person.objects.create(first_name='John', last_name='Shaw', phone_no='1234',
                                    email_id='john@test.com', description='This is my description')
    school1 = School.objects.create(school='UIUC')
    Education.objects.create(school=school1, degree_name='MS',
                             start_date='2021-08-19', gpa='4', person_id=person1)
    Experience.objects.create(company_name='Bayer', job_title='Intern',
                              start_date='2021-05-16', description='My description', person_id=person1)
    project = Project.objects.create(project_title='Test title', start_date='2021-05-16')
    project.persons.add(person1)
    skill = Skill.objects.create(skill_name='Python', proficiency=proficiency)
    skill.persons.add(person1)














