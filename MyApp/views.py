from django.shortcuts import render
from . models import StudentModel
from . serializers import StudentSerializer
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# Create your views here.



class api_view(APIView):

    def get(self,request):

        studentdata=StudentModel.objects.all() #complex data querset
        #convert complex data into python native datatype 
        python_data=StudentSerializer(studentdata,many = True)

        #python native data to simple data (json)

        # josn_data=JSONRenderer().render(python_data.data)
        # # print(josn_data)

        # return Response(josn_data)
    
        return JsonResponse(python_data.data , safe=False)

    def post(self,request):
        data=request.data
        print(data)
        serializer=StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({'msg':'successfully'})

        return Response(serializer.errors)
    



def home_view(request):
    return render (request,'home.html')