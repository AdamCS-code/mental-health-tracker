from django.forms import ModelForm
from main.models import MoodEntry
#lalalala
class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["mood", "feelings", "mood_intensity"]