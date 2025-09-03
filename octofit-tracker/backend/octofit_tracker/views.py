
import os
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET', 'POST'])
def api_root(request, format=None):
	if request.method == 'POST':
		return Response({"message": "POST request received"}, status=status.HTTP_201_CREATED)


	# Dynamically build Codespace URL
	codespace_name = 'curly-robot-p7pj9x7gg5r39rv5'
	if codespace_name:
		CODESPACE_URL = f'https://{codespace_name}-8000.app.github.dev/'
	else:
		CODESPACE_URL = 'http://localhost:8000/'

	API_SUFFIX = getattr(settings, 'CODESPACE_API_SUFFIX', '/api/')

	return Response({
		'users': CODESPACE_URL + f'{API_SUFFIX}users/?format=api',
		'teams': CODESPACE_URL + f'{API_SUFFIX}teams/?format=api',
		'activity': CODESPACE_URL + f'{API_SUFFIX}activity/?format=api',
		'leaderboard': CODESPACE_URL + f'{API_SUFFIX}leaderboard/?format=api',
		'workouts': CODESPACE_URL + f'{API_SUFFIX}workouts/?format=api',
		'users_local': 'http://localhost:8000/' + f'{API_SUFFIX}users/?format=api',
		'teams_local': 'http://localhost:8000/' + f'{API_SUFFIX}teams/?format=api',
		'activity_local': 'http://localhost:8000/' + f'{API_SUFFIX}activity/?format=api',
		'leaderboard_local': 'http://localhost:8000/' + f'{API_SUFFIX}leaderboard/?format=api',
		'workouts_local': 'http://localhost:8000/' + f'{API_SUFFIX}workouts/?format=api',
	})

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer
