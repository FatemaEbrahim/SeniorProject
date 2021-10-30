from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

class StudentAuthBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username, password):
        try:
            student = Student.objects.get(academic_id=username)
            success = check_password(password, student.password)
            if success:
                return student
        except Student.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            raise ValueError('Student does not exist')
        return None

    def get_user(self, uid):
        try:
            return Student.objects.get(pk=uid)
        except Student.DoesNotExist:
            return None

    def logout(request, user):
        """
        Remove the authenticated user's ID from the request and flush their session
        data.
        """
        # Dispatch the signal before the user is logged out so the receivers have a
        # chance to find out *who* logged out.
        user = getattr(request, 'user', None)
        if not getattr(user, 'is_authenticated', True):
            user = None
        user_logged_out.send(sender=user.__class__, request=request, user=user)
        request.session.flush()
        if hasattr(request, 'user'):
            from django.contrib.auth.models import AnonymousUser
            request.user = AnonymousUser()