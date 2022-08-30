from rest_framework import serializers
from portfolios.models import Portfolio, Photo


class PhotoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)
    description = serializers.CharField(default='')
    img = serializers.ImageField(allow_null=False, allow_empty_file=False)
    portfolio_name = serializers.CharField(source="portfolio.name", read_only=True)
    portfolio_id = serializers.IntegerField(write_only=True, )

    class Meta:
        model = Photo
        fields = ('id', 'name', 'description', 'img', 'portfolio_name', 'portfolio_id', )

    def create(self, validated_data):
        request = self.context.get("request")
        portfolio_id = validated_data['portfolio_id']
        portfolio_obj = Portfolio.objects.filter(user_created=request.user).filter(id=portfolio_id).first()
        if not portfolio_obj:
            raise serializers.ValidationError(
                'Portfolio does not exist'
            )
        validated_data['portfolio'] = portfolio_obj
        return Photo.objects.create(**validated_data)


class PortfolioSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)
    description = serializers.CharField(default='')
    portfolio_images = serializers.SerializerMethodField('get_portfolio_images')
    user_created = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_portfolio_images(self, obj):
        portfolio_images_query = Photo.objects.filter(portfolio=obj)
        serializer = PhotoSerializer(portfolio_images_query, many=True)
        return serializer.data

    def create(self, validated_data):
        obj, created = Portfolio.objects.get_or_create(**validated_data)
        if not created:
            raise serializers.ValidationError(
                'Such a portfolio already exists'
            )
        else:
            return obj

    class Meta:
        model = Portfolio
        fields = ('id', 'name', 'description', 'portfolio_images', 'user_created')
