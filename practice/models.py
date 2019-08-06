from django.db import models

class user(models.Model):
    user_name = models.CharField(max_length=255, primary_key=True)
    email = models.EmailField(default="kane@99.com")
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")

    class Meta:
        ordering = ('user_name',)

    def __str__(self):
        return self.user_name

class receipt(models.Model):
    name = models.CharField(max_length=255, null=False)
    user_name = models.OneToOneField(user, on_delete=models.CASCADE, default="")
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class step(models.Model):
    text = models.CharField(max_length=255, null=False)
    receipt = models.ForeignKey(receipt, on_delete=models.CASCADE, default="")

    class Meta:
        ordering = ('text',)

    def __str__(self):
        return self.text

class ingredient(models.Model):
    text = models.CharField(max_length=255, null=False)
    receipt = models.ForeignKey(receipt, on_delete=models.CASCADE, default="")

    class Meta:
        ordering = ('text',)

    def __str__(self):
        return self.text

