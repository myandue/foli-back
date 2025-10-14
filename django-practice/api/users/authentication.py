from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 커스텀 인증 로직 구현
        user = None  # 실제로는 요청에서 사용자 정보를 추출하여 인증해야 함
        if not user:
            raise AuthenticationFailed("사용자를 인증할 수 없습니다.")
        return (user, None)
