from django.db import models
from django.contrib.auth.models import (
    Permission, Group, BaseUserManager, AbstractBaseUser, PermissionsMixin)
# from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

Permission.add_to_class('description', models.TextField(max_length=255, null=True, blank=True))
Permission.add_to_class('is_active', models.BooleanField(default=True))
Group.add_to_class('is_active', models.BooleanField(default=True))

class Role(Group):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        # Creates and saves a User with the given username and password.
        # If using email then normalize it
        if not username:
            raise ValueError('Users must have username')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password):
        # Creates and saves a staff user with the given email and password.
        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        # Creates and saves a superuser with the given email and password.
        user = self.create_user(username, email, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=50,
        unique=True,
        null=False,
        blank=False,
    )   # you can insert validator here
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.active

    # @property
    # def groups(self):
    #     return self.roles