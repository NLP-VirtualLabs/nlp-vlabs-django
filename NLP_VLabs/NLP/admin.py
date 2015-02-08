from django.contrib import admin

from NLP.models import User_Profile
from NLP.models import Experiments
from NLP.models import Experiment_Stage
from NLP.models import User_Experiments
from NLP.models import User_Experiment_Stage

# Register your models here.
admin.site.register(User_Profile)
admin.site.register(Experiments)
admin.site.register(Experiment_Stage)
admin.site.register(User_Experiments)
admin.site.register(User_Experiment_Stage)
