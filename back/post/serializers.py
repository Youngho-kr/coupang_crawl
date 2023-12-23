from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "discount_percent",
            "old_price",
            "new_price",
        )
        model = Post
    