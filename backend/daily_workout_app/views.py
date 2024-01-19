from django.shortcuts import get_object_or_404
from django.utils import timezone
from user_app.views import UserPermissions
from rest_framework.response import Response
from .serializers import DaySerializer, WorkoutSerializer, Day, Workout
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

# Create your views here.


class All_Days(UserPermissions):
    def post(self, request):
        request.data["user"] = request.user
        new_day = DaySerializer(data=request.data)
        if new_day.is_valid():
            new_day.save()
            return Response(
                "Congrats new daily activity was created!", HTTP_201_CREATED
            )
        else:
            print(new_day.error_messages)
            return Response(new_day.error_messages, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(DaySerializer(request.user.days.all(), many=True).data)


class A_day(UserPermissions):
    def get_a_day(self, request, id):
        return get_object_or_404(request.user.days, id=id)

    def get(self, request, id):
        return Response(DaySerializer(self.get_a_day(request, id)).data)

    def delete(self, request, id):
        day = self.get_a_day(request, id)
        day.delete()
        return Response("Day and workouts on this day have been deleted")


class All_workouts(UserPermissions):
    def get(self, request):
        return Response(WorkoutSerializer(request.user.workouts.all(), many=True).data)

    def post(self, request):
        user = request.user
        day, created = Day.objects.get_or_create(
            date=request.data.get("date", timezone.now().date()), user=user
        )
        name = request.data.get("name")
        data = {"user": user, "day": day, "name": name}
        new_workout = Workout(**data)
        del data["user"]
        new_workout_ser = WorkoutSerializer(data=data)
        if new_workout_ser.is_valid():
            new_workout.save()
            return Response(new_workout_ser.data, status=HTTP_201_CREATED)
        else:
            print("failed to create workout")
            # print(new_workout_ser.error_messages)
            return Response(new_workout_ser.error_messages, status=HTTP_400_BAD_REQUEST)


class A_workout(UserPermissions):
    def get_a_workout(self, request, id):
        return get_object_or_404(request.user.workouts, id=id)

    def get(self, request, id):
        return Response(WorkoutSerializer(self.get_a_workout(request, id)).data)

    def put(self, request, id):
        workout = self.get_a_workout(request, id)
        updated_workout = WorkoutSerializer(workout, data=request.data, partial=True)
        if updated_workout.is_valid():
            updated_workout.save()
            return Response(updated_workout.data)
        else:
            print(updated_workout.error_messages)
            return Response(updated_workout.error_messages, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        workout = self.get_a_workout(request, id)
        day = workout.day
        workout.delete()
        if not len(day.workouts.all()):
            day.delete()
        return Response("This workout has been deleted")
