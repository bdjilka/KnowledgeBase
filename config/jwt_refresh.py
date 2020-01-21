from rest_framework_jwt.settings import api_settings

if api_settings.JWT_AUTH_COOKIE:
    from rest_framework_jwt.authentication import JSONWebTokenAuthentication
    from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
    from rest_framework_jwt.views import RefreshJSONWebToken

    RefreshJSONWebTokenSerializer._declared_fields.pop('token')

    class RefreshJSONWebTokenSerializerCookieBased(RefreshJSONWebTokenSerializer):
        def validate(self, attrs):
            if 'token' not in attrs:
                if api_settings.JWT_AUTH_COOKIE:
                    attrs['token'] = JSONWebTokenAuthentication().get_jwt_value(self.context['request'])
            return super(RefreshJSONWebTokenSerializerCookieBased, self).validate(attrs)

    RefreshJSONWebToken.serializer_class = RefreshJSONWebTokenSerializerCookieBased
