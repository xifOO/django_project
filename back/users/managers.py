from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_User(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Enter email')
        if not username:
            raise ValueError('Enter username')
        if not password:
            raise ValueError('Enter password')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self.create_User(email, username, password)

    def create_superuser(self, email, username, password):
        return self.create_User(email, username, password, is_staff=True, is_superuser=True)

