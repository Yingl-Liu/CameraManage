from snippets.models import CameraInfo,RecombinationNode#,Image
from rest_framework import serializers

class CuttingNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CameraInfo
        fields=('id','ip','isOnLine','coordinate'
                # ,'x','y','xa','ya','xb','yb','xc','yc','xd','yd','cuttingXList','cuttingYList','transformMat','toploMat'
                )
     
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CameraInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.ip = validated_data.get('ip', instance.ip)
        instance.isOnLine = validated_data.get('isOnLine', instance.isOnLine)
        instance.coordinate=validated_data.get('coordinate',instance.coordinate)
        # instance.x = validated_data.get('x', instance.x)
        # instance.y = validated_data.get('y', instance.y)
        # instance.xa = validated_data.get('xa', instance.xa)
        # instance.ya = validated_data.get('ya', instance.ya)
        # instance.xb = validated_data.get('xb', instance.xb)
        # instance.yb = validated_data.get('yb', instance.yb)
        # instance.xc = validated_data.get('xc', instance.xc)
        # instance.yc = validated_data.get('yc', instance.yc)
        # instance.xd = validated_data.get('xd', instance.xd)
        # instance.yd = validated_data.get('yd', instance.yd)
        # instance.cuttingXList = validated_data.get('cuttingXList', instance.cuttingXList)
        # instance.cuttingYList = validated_data.get('cuttingYList', instance.cuttingYList)
        # instance.transformMat = validated_data.get('transformMat', instance.transformMat)
        # instance.toploMat = validated_data.get('toploMat', instance.toploMat)
        instance.save()
        return instance

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Image
#         fields=('id','ip','image')
#
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Image.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.id = validated_data.get('id', instance.id)
#         instance.ip = validated_data.get('ip', instance.ip)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()
#         return instance
class RecombinationNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecombinationNode
        fields=('id','ip','isTimedRecording','startTime','duration')
      
     
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return RecombinationNode.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.ip = validated_data.get('ip', instance.ip)
        # instance.toploMat = validated_data.get('toploMat', instance.toploMat)
        # instance.position = validated_data.get('position', instance.position)
        instance.isTimedRecording = validated_data.get('isTimedRecording',instance.isTimedRecording)
        instance.startTime = validated_data.get('startTime',instance.startTime)
        instance.duration = validated_data.get('duration',instance.duration)
        instance.save()
        return instance
