import imp
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

User = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id','username','token','first_name','last_name' )

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('telephone','email','representer','company_name','password', 'password2', 'username',)
        extra_kwargs = {'email': {'required': True},'telephone': {'required': True},'company_name': {'required': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   telephone=validated_data['telephone'],
                                   email=validated_data['email'],
                                   company_name=validated_data['company_name'],
                                   representer=validated_data['representer'],
                                   )
        user.set_password(validated_data['password'])
        user.save()
        return user
