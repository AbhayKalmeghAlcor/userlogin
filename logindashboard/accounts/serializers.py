from .models import Account, UserProfile
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = '__all__'

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = '__all__'

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'is_admin' ]


class UserprofileSerializer(serializers.ModelSerializer):
    user = AccountSerializer()

    class Meta:
        model = UserProfile
        fields = ('id', 'manager_email','hire_date','birth_date','country','department','location','role','avtar', 'allowance_boost','user_mode','user')

    def get_account_data(self, obj):
        userprofile_serializer = AccountSerializer(obj.user)
        return userprofile_serializer.data

    # def create(self, validated_data):
    #     user = UserProfile.objects.create(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
