from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quiz.models import Quiz
import time

def qpage(request):
	questions = Quiz.objects.all()
	print("loaded")
	print("ques",questions)

	return render(request, 'quiz.html', { 'questions': questions})
	
def page_load(request):
	print("page_load")
	questions = Quiz.objects.all()
	print("question",questions)
	return Response(questions,status=status.HTTP_200_OK)