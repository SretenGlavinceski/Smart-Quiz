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
