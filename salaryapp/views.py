from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib
def index(request):

    donnees={
        'nom':'jiresse',
        'postnom':'musubao',
        'sexe':'Masculin'
    }

    template=loader.get_template('index.html')
    return HttpResponse(template.render(donnees,request))


def salary(request):
    template=loader.get_template('learning.html')
    return HttpResponse(template.render({},request))

def predire(request):
   
    if request.method=='POST':

        alloc_fam=int(request.POST['alloc_fam'])
        niv_etud=int(request.POST['niv_etud'])
        type_ecole=int(request.POST['type_ecole'])
        age=int(request.POST['age'])
        ann_exp=int(request.POST['ann_exp'])

        
        tableau=[[alloc_fam,niv_etud,type_ecole,age,ann_exp]]
        print(tableau)

        
        regresseur=joblib.load('modele_lm/dataset_teacherV1.pkl')
        resultat=regresseur.predict(tableau)
        
        print(resultat)


    return HttpResponse('ok')
