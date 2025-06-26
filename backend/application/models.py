from django.db import models


class Section(models.Model):
    section_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.section_name


class Question(models.Model):
    question_text = models.TextField(null=True, blank=True)
    section = models.ForeignKey(Section, related_name='questions', on_delete=models.CASCADE, null=True, blank=True)
    correct_answer = models.ForeignKey('AnswerOption', on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='correct_for_questions')
    points_question = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.question_text


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, related_name='answer_options', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.answer_text}'