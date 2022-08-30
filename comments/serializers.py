from rest_framework import serializers

from comments.models import Comment
from portfolios.models import Photo


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=150, allow_null=True)
    message = serializers.CharField(allow_null=False, allow_blank=False, min_length=2)
    photo_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ('user_name', 'message', 'photo_id')

    def create(self, validated_data):
        photo_id = validated_data['photo_id']
        photo_obj = Photo.objects.filter(id=photo_id).first()
        if not photo_obj:
            raise serializers.ValidationError(
                'Photo does not exist'
            )
        validated_data['photo'] = photo_obj
        return Comment.objects.create(**validated_data)
