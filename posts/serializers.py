from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_serializer_extensions.fields import HashIdField
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin
from rest_framework_serializer_extensions.utils import (
    external_id_from_model_and_internal_id,
)

from authentication.serializers import UserSerializer
from hunchat.model_loaders import get_post_like_model, get_post_model
from videos.serializers import VideoSerializer


class PostSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=get_post_model(), read_only=True)
    video = VideoSerializer()
    author = UserSerializer()
    comment_to = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_post_model()
        fields = [
            "id",
            "description",
            "video",
            "resources_link",
            "author",
            "created_at",
            "comment_to",
            "comments",
            "comments_count",
            "likes",
            "likes_count",
        ]
        read_only_fields = [
            "id",
            "comment_to",
        ]

    def get_comment_to(self, obj):
        comment_to = obj.comment_to
        if comment_to:
            serializer = PostCommentToSerializer(comment_to)
            return serializer.data
        return None

    def get_comments(self, obj):
        comments = obj.get_comments()
        serializer = PostCommentSerializer(comments, many=True)
        return serializer.data

    def get_comments_count(self, obj):
        return obj.get_comments_count()

    def get_likes(self, obj):
        likes = obj.get_likes()
        serializer = PostLikeShortSerializer(likes, many=True)
        return serializer.data

    def get_likes_count(self, obj):
        return obj.get_likes_count()


class PostCommentToSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=get_post_model(), read_only=True)
    video = VideoSerializer()

    class Meta:
        model = get_post_model()
        fields = [
            "id",
            "video",
        ]
        read_only_fields = [
            "id",
        ]


class PostCommentSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=get_post_model(), read_only=True)
    video = VideoSerializer()
    author = UserSerializer()

    class Meta:
        model = get_post_model()
        fields = [
            "id",
            "video",
            "author",
        ]
        read_only_fields = [
            "id",
        ]


class PostLikeUserIdSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=get_user_model(), read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
        ]


class PostLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = get_post_like_model()
        fields = [
            "user",
            "post",
        ]


class PostLikeShortSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=get_post_like_model(), read_only=True)
    user = PostLikeUserIdSerializer()

    class Meta:
        model = get_post_like_model()
        fields = [
            "id",
            "user",
        ]


class PostThreadSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=get_post_model(), read_only=True)
    thread = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_post_model()
        fields = ["id", "thread"]
        read_only_fields = [
            "id",
            "thread",
        ]

    def get_thread(self, obj):
        thread = obj.get_thread()
        serializer = PostSerializer(thread, many=True)
        return serializer.data
