from rest_framework import serializers
from .models import Movie, Review, Rating

class MovieListSerializer(serializers.ModelSerializer):
    """ Вывод списка фильмов """

    class Meta:
        model = Movie
        fields = ('title','tagline')

class ReviewCreateSerializer(serializers.ModelSerializer):
    """ Добавление отзывов """

    class Meta:
        model = Review
        fields = '__all__'

class RecursiveSerializer(serializers.Serializer):
    """ Вывод вложеных коментариев """
    def to_representation(self,value):
        print(value)
        print(self)
        print(self.parent)
        print(self.parent.parent)
        print(self.context)
        print("==========================================================")
        serializer = self.parent.parent.__class__(value,context=self.context)
        return serializer.data

class FilterReviewListSerializer(serializers.ListSerializer):
    """ Фильтр коментариев """
    def to_representation(self,data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class ReviewSerializer(serializers.ModelSerializer):
    """ Вывод отзывов  """
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ('name','text',"children")

class MovieDetailSerializer(serializers.ModelSerializer):
    """ Вывод фильмов """
    category = serializers.SlugRelatedField(slug_field='name',read_only=True)
    directors = serializers.SlugRelatedField(slug_field='name',read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name',read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name',read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ('draft',)

class AddRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('star','movie')
    
    def create(self, validate_data):
        rating =Rating.objects.update_or_create(
            ip = validate_data.get('ip',None),
            movie = validate_data.get('movie',None),
            defaults={'star':validate_data.get('star')}
        )
        print(rating)
        print("Create")
        return rating
