from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here. 
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination




from django_filters.rest_framework import DjangoFilterBackend

# def student_detail(request):
#     stu=Student.objects.get(id=1)
#     print(stu)
#     serializer=StudentSerializer(stu)
#     print(serializer)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')

# def student_data(request,pk):
#     stu=Student.objects.get(id=pk)
#     print(stu)
#     serializer=StudentSerializer(stu)
#     print(serializer)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')

# # query set
# def student_list(request):
#     stu=Student.objects.all()
#     serializer=StudentSerializer(stu,many=True)
#     # json_data=JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data,content_type='application/json')
#     # other method jsonresponse
#     return JsonResponse(serializer.data,safe=False)


#-----------------------------------------------------------------------------------------------

#PageNumberPagination

# class stupagination(PageNumberPagination):
#     page_size=3  # means number of records
#     page_size_query_param='records'  #client set manually  see records
#     max_page_size=5                  # max 5 record 

#-------------------------------------------------------------

# offset pagination

# class stupagination1(LimitOffsetPagination):
#    pass
#-------------------------------------------------------------

# cursor  pagination

# class stupagination2(CursorPagination):
#    page_size=3
# #    ordering='name'


class StudentList(ListAPIView):
    # queryset=Student.objects.filter(city='ahmedabad')
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['name','city']
    # filter_backends=[SearchFilter]
    # search_fields=['city','name']
    # # search_fields=['^name']
    # filter_backends=[OrderingFilter]
    # ordering_fields=['name']
   
    # ordering_fields='__all__'
    
    
    # pagination_class=stupagination
    # pagination_class=stupagination1
    # pagination_class=stupagination2
   

    




class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        try:
            id=pk
            if id is not None:
                stu=Student.objects.get(id=id)
                serializer=StudentSerializer(stu)
                return Response(serializer.data)
            
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
        
        except Student.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
         
            
    
    @csrf_exempt
    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':status.HTTP_201_CREATED,'msg':'data created'},status=status.HTTP_201_CREATED)
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            
            

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.errors)
   
    def delete(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})

