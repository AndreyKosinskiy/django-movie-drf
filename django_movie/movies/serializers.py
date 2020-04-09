from rest_framework import serializers
from .models import Movie, Review

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

class ReviewSerializer(serializers.ModelSerializer):
    """ Вывод отзывов  """

    class Meta:
        model = Review
        fields = ('name','text','parent' )

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