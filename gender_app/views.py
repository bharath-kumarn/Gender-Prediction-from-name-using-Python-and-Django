from django.shortcuts import render
from django.views import View
from gender_predictor import GenderPredictor
from .forms import NameForm


class GenderPrediction(View):

    def get(self, request, *arg, **kwargs):
        gp = GenderPredictor()
        gp.train_and_test()
        context = {
            "form": NameForm,
        }
        return render(request, 'gender_app/home.html',context)

    def post(self, request, **kwargs):
        if 'submit' in request.POST:

            name=request.POST['name']
            gp = GenderPredictor()
            gp.train_and_test()
            detected_gender = gp.classify(name)
            context = {
                "name" : name,
                "gender": detected_gender

            }
            return render(request, 'gender_app/predict_gender.html',context)

