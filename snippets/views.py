from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import CameraInfo,RecombinationNode#,Image
from snippets.serializers import CuttingNodeSerializer,RecombinationNodeSerializer#,ImageSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import os
def pointinrect(p=[],x=None,y=None):
    ncross=0
    for i in range(0,8,2):
        p1x=p[i]
        p1y=p[i+1]
        p2x=p[(i+2)%8]
        p2y=p[(i+3)%8]
        if p1y==p2y:
            continue
        if y<min(p1y,p2y):
            continue
        if y>max(p1y,p2y):
            continue
        jx =float(y - p1y)*float(p2x-p1x)/float(p2y-p1y)+p1x
        if jx>x:
            ncross=ncross+1
    return ncross%2==1
        
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        

@api_view(['GET', 'POST'])
def snippet_list(request,format=None):
    """
    展示所有存在的snippet, 或建立新的snippet
    """
    if request.method == 'GET':
      snippets = CameraInfo.objects.all()
      serializer = CuttingNodeSerializer(snippets, many=True)
      return Response(serializer.data)

    elif request.method == 'POST':
     #  data = stream.read().decode(encoding)
      
      serializer = CuttingNodeSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def snippet_search(request,x1,y1,x2,y2,x3,y3,x4,y4,format=None):
       if request.method == 'GET':
        # snippets = Snippet.objects.filter(x=x1)
        snippets = CameraInfo.objects.values()
        a=[float(x1),float(y1),float(x2),float(y2),float(x3),float(y3),float(x4),float(y4)]
        b=[]
        for e in snippets:
            if pointinrect(a,float(e['x']),float(e['y'])):
                 b.append(e)
        serializer = CuttingNodeSerializer(b, many=True)
        # numbers=JSONResponse(serializer.data)
       #  b=[x1,y1]
        return Response(serializer.data)  

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    展示, 更新或删除一个snippet
    """
    try:
      snippet = CameraInfo.objects.get(pk=pk)
    except CameraInfo.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      serializer = CuttingNodeSerializer(snippet)
      return Response(serializer.data)

    elif request.method == 'PUT':
      serializer = CuttingNodeSerializer(snippet, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      snippet.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def image_list(request,format=None):
#     """
#     展示所有存在的snippet, 或建立新的snippet
#     """
#     if request.method == 'GET':
#       snippets = Image.objects.all()
#       serializer = ImageSerializer(snippets, many=True)
#       return Response(serializer.data)
#
#     elif request.method == 'POST':
#      #  data = stream.read().decode(encoding)
#
#       serializer = ImageSerializer(data=request.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'PUT', 'DELETE'])
# def image_detail(request, pk):
#     """
#     展示, 更新或删除一个snippet
#     """
#     try:
#       snippet = Image.objects.get(pk=pk)
#     except snippet.DoesNotExist:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#       serializer = ImageSerializer(snippet)
#       return Response(serializer.data)
#
#     elif request.method == 'PUT':
#       serializer = ImageSerializer(snippet, data=request.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#       image=Image.objects.values('id','image')
#       for iddata in image:
#             if int(iddata['id'])==int(pk):
#                filename='/home/atr/picture/'+iddata['image']
#                os.remove(filename)
#                break
#       snippet.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def mat_list(request,format=None):
    """
    展示所有存在的snippet, 或建立新的snippet
    """
    if request.method == 'GET':
      snippets = RecombinationNode.objects.all()
      serializer =RecombinationNodeSerializer(snippets, many=True)
      return Response(serializer.data)

    elif request.method == 'POST':
     #  data = stream.read().decode(encoding)
      
      serializer = RecombinationNodeSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def mat_detail(request, pk):
    """
    展示, 更新或删除一个snippet
    """
    try:
      snippet = RecombinationNode.objects.get(pk=pk)
    except RecombinationNode.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      serializer = RecombinationNodeSerializer(snippet)
      return Response(serializer.data)

    elif request.method == 'PUT':
      serializer = RecombinationNodeSerializer(snippet, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      snippet.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
