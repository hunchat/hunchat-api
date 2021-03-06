from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Notification(models.Model):
    owner = models.ForeignKey(
        "authentication.User", related_name="notifications", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)

    POST_COMMENT = "PC"
    POST_LIKE = "PL"

    NOTIFICATION_TYPES = (
        (POST_COMMENT, "Post Comment"),
        (POST_LIKE, "Post Like"),
    )

    notification_type = models.CharField(max_length=3, choices=NOTIFICATION_TYPES)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        ordering = ["-created_at"]


class PostCommentNotificationManager(models.Manager):
    def create(self, *args, **kwargs):
        post_comment_notification = super(PostCommentNotificationManager, self).create(
            post_comment=kwargs["post_comment"]
        )
        Notification.objects.create(
            owner_id=kwargs["owner_id"],
            notification_type=Notification.POST_COMMENT,
            content_object=post_comment_notification,
        )
        return post_comment_notification


class PostCommentNotification(models.Model):
    notification = GenericRelation("notifications.Notification")
    post_comment = models.ForeignKey("posts.Post", on_delete=models.CASCADE)

    objects = PostCommentNotificationManager()


class PostLikeNotificationManager(models.Manager):
    def create(self, *args, **kwargs):
        post_like_notification = super(PostLikeNotificationManager, self).create(
            post_like=kwargs["post_like"]
        )
        Notification.objects.create(
            owner_id=kwargs["owner_id"],
            notification_type=Notification.POST_LIKE,
            content_object=post_like_notification,
        )
        return post_like_notification


class PostLikeNotification(models.Model):
    notification = GenericRelation("notifications.Notification")
    post_like = models.ForeignKey("posts.PostLike", on_delete=models.CASCADE)

    objects = PostLikeNotificationManager()
