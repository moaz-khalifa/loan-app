from django.db import models
from django.conf import settings


class Loan(models.Model):
    amount = models.IntegerField()
    term = models.IntegerField()
    status = models.CharField(
        choices=[("pending", "pending"), ("approved", "approved"),
                 ("rejected", "rejected")],
        default="pending",
        max_length=200
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return f"{self.pk}"
