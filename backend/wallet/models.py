from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from users.models import User
import uuid


class Transaction(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
  from_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='from_transactions')
  from_id = models.PositiveIntegerField()
  from_object = GenericForeignKey('from_type', 'from_id')
  from_amount = models.FloatField(blank=False, null=False)
  to_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='to_transactions')
  to_id = models.PositiveIntegerField()
  to_object = GenericForeignKey('to_type', 'to_id')
  created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
  updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)


class Wallet(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100, default='Default wallet')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallets')


class Asset(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='assets')
  asset_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  asset_id = models.PositiveIntegerField()
  asset_object = GenericForeignKey('asset_type', 'asset_id')
  asset_amount = models.FloatField(blank=False, null=False)