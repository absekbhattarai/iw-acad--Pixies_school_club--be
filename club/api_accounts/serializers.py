from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginAdminSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            first_name=self.validated_data['first_name'],
            middle_name=self.validated_data['middle_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'Password do not match'})
        user.set_password(password)
        user.save()
        return user

