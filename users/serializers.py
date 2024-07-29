from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields: tuple = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        """
        Create a new user.
        :param validated_data: user data
        :return: user instance
        """
        password = validated_data.pop('password', None)
        instance = User.objects.create(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
