from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.utils import timezone
from .models import Day, Workout
from user_app.serializers import UserSerializer
import pytz


class OnlyDaySerializer(ModelSerializer):
    date = SerializerMethodField()

    class Meta:
        model = Day
        fields = ["date"]

    def get_date(self, obj):
        pst_timezone = pytz.timezone("America/Los_Angeles")
        utc_timezone = timezone.make_aware(
            timezone.datetime(obj.date.year, obj.date.month, obj.date.day)
        )
        return utc_timezone.astimezone(pst_timezone).date()


class WorkoutSerializer(ModelSerializer):
    day = OnlyDaySerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = ["id", "day", "user", "name"]


class DaySerializer(ModelSerializer):
    workouts = WorkoutSerializer(many=True)

    class Meta:
        model = Day
        fields = ["id","date", "workouts"]
