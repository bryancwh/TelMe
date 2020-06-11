from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        """Allow authenticate with email"""

        if email is None and password is None:
            return

        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user
