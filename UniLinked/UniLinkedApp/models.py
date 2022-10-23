from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 200)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.user
    
class MyAccountManager(BaseUserManager):
	def create_user(self, username, password=None, **extra_fields):
		if not username:
			raise ValueError("Users must have an username")

		user  = self.model(
                username=username,
                password = password,
                **extra_fields
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password):
		user  = self.create_user(
                username=username,
				password=password,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
    
    username                = models.CharField(max_length = 200)
    email                   = models.EmailField(max_length = 200)
    password                = models.CharField(max_length = 200)
    university              = models.CharField(max_length=50)
    major                   = models.CharField(max_length = 200)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

