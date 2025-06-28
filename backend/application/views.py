from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Section, Question
from .serializers import SectionSerializer, QuestionSerializer


@api_view(['GET'])
def get_sections(request):
    sections = Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_questions_by_section(request, section_id):
    questions = Question.objects.filter(section_id=section_id)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Section, Question, AnswerOption
import json

@csrf_exempt
def add_question_to_section(request, section_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            section = Section.objects.get(id=section_id)
            question = Question.objects.create(section=section, question_text=data['text'])

            # Create all AnswerOption objects first
            answer_options = []
            for ans in data['answers']:
                answer_option = AnswerOption.objects.create(
                    question=question,
                    answer_text=ans['text']
                )
                answer_options.append(answer_option)

            correct_index = None
            for i, ans in enumerate(data['answers']):
                if ans.get('is_correct'):
                    correct_index = i
                    break

            if correct_index is not None:
                question.correct_answer = answer_options[correct_index]
                question.save()

            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)