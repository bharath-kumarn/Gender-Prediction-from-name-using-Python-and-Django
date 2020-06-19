# from .views import AssetCastCrew, ContentCastCrew
from django.urls import path
from .views import GenderPrediction

urlpatterns = [

    # Gender Prediction
    path('home/', GenderPrediction.as_view(), name='gender_prediction'),
]

