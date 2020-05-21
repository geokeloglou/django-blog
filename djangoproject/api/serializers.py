from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted', 'author']

# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password2']
#         # extra_kwargs = {
#         #     'password': {'write_only': True}
#         # }

#     def save(self):
#         user = User.objects.create_user(
#             email = self.validated_data['email'],
#             username = self.validated_data['username'],
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match!'})

#         user.set_password(password)
#         user.save()
#         return User

