from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET', 'POST'])
def api_root(request, format=None):
	if request.method == 'POST':
		return Response({"message": "POST request received"}, status=status.HTTP_201_CREATED)

	# Use Codespace URL if available, otherwise fallback to localhost
	CODESPACE_URL = 'https://curly-robot-p7pj9x7gg5r39rv5-8000.app.github.dev/'
	LOCAL_URL = 'http://localhost:8000/'
	return Response({
		'users': CODESPACE_URL + 'api/users/?format=api',
		'teams': CODESPACE_URL + 'api/teams/?format=api',
		'activity': CODESPACE_URL + 'api/activity/?format=api',
		'leaderboard': CODESPACE_URL + 'api/leaderboard/?format=api',
		'workouts': CODESPACE_URL + 'api/workouts/?format=api',
		'users_local': LOCAL_URL + 'api/users/?format=api',
		'teams_local': LOCAL_URL + 'api/teams/?format=api',
		'activity_local': LOCAL_URL + 'api/activity/?format=api',
		'leaderboard_local': LOCAL_URL + 'api/leaderboard/?format=api',
		'workouts_local': LOCAL_URL + 'api/workouts/?format=api',
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
