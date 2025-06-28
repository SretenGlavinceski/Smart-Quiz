from django.contrib.auth import get_user_model
from application.models import Section, Question, AnswerOption

User = get_user_model()

username = 'admin'
password = 'admin'
email = ''

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Created superuser")

if Section.objects.count() == 0:
    s1 = Section.objects.create(section_name="Math", description="Math quizzes for testing you math skills.")
    s2 = Section.objects.create(section_name="Science", description="Science quizzes for feature scientists.")
    print("Created sample sections")

    # Sample questions for Math
    q1 = Question.objects.create(
        question_text="What is 2 + 2?",
        section=s1,
        points_question=1
    )
    a1_1 = AnswerOption.objects.create(question=q1, answer_text="3")
    a1_2 = AnswerOption.objects.create(question=q1, answer_text="4")
    a1_3 = AnswerOption.objects.create(question=q1, answer_text="5")
    a1_4 = AnswerOption.objects.create(question=q1, answer_text="6")
    q1.correct_answer = a1_2
    q1.save()

    q2 = Question.objects.create(
        question_text="What is 10 / 2?",
        section=s1,
        points_question=1
    )
    a2_1 = AnswerOption.objects.create(question=q2, answer_text="2")
    a2_2 = AnswerOption.objects.create(question=q2, answer_text="5")
    a2_3 = AnswerOption.objects.create(question=q2, answer_text="10")
    a2_4 = AnswerOption.objects.create(question=q2, answer_text="20")
    q2.correct_answer = a2_2
    q2.save()

    # Sample questions for Science
    q3 = Question.objects.create(
        question_text="What planet is known as the Red Planet?",
        section=s2,
        points_question=1
    )
    a3_1 = AnswerOption.objects.create(question=q3, answer_text="Earth")
    a3_2 = AnswerOption.objects.create(question=q3, answer_text="Mars")
    a3_3 = AnswerOption.objects.create(question=q3, answer_text="Jupiter")
    a3_4 = AnswerOption.objects.create(question=q3, answer_text="Venus")
    q3.correct_answer = a3_2
    q3.save()

    print("Created sample questions and answers")
else:
    print("Sections already exist, skipping sample data creation")
