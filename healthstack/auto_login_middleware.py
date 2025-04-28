from django.contrib.auth import login, get_user_model
from django.utils.deprecation import MiddlewareMixin

User = get_user_model()

class AutoLoginSuperUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if hasattr(request, 'user') and not request.user.is_authenticated:
            try:
                user = User.objects.filter(is_superuser=True).first()
                if user:
                    print(f"Logging in as: {user.username}")  # Debug print
                    login(request, user)
            except Exception as e:
                print("Auto login error:", e)
