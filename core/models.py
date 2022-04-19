from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, username='', is_staff=False, is_admin=False, is_active=True):
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.username = username
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password):
        user = self.create_user(email, password, is_staff=True, is_admin=True, is_active=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True
    )

    avatar = models.ImageField(
        upload_to='',
        default='avatars/default.png'
    )

    username = models.CharField(
        max_length=50
    )

    date_register = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField()
    is_admin = models.BooleanField()
    is_staff = models.BooleanField()

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        if self.username is None:
            return 'Admin'
        else:
            return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Coin(models.Model):
    name = models.CharField(
        max_length=100
    )

    buy_price = models.FloatField()

    coin_price = models.FloatField()

    date = models.DateTimeField(
        auto_now=True
    )

    amount = models.FloatField(default=0, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'


class Portfolio(models.Model):
    name = models.CharField(
        max_length=50
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users'
    )

    coins = models.ManyToManyField(
        Coin,
        related_name='coins',
        blank=True,
    )

    date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
