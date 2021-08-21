from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser


class PostArticle(models.Model):
    """
    This class creates post-page.
    """
    title = models.CharField(max_length=255)
    # 記事URL
    url = models.URLField()
    # なにか個人的感想があれば
    text = models.TextField(null=True)
    author = models.CharField(max_length=30)
    # 作成日
    create_at = models.DateField(auto_now_add=True)
    # 更新日
    updated_at = models.DateField(auto_now=True)

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Comment(models.Model):

    comment = models.TextField(default="", max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    # on_deleteとはuserがのちに削除された際に、コメントも削除される（CASCADE）
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    article = models.ForeignKey(PostArticle, on_delete=models.CASCADE)