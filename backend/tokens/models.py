from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
import uuid

# Create your models here.
class CryptoCurrency(models.Model):
  class Meta:
    verbose_name = "Crypto Currency"
    verbose_name_plural = "Crypto Currencies"
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  symbol = models.CharField(max_length=5, unique=True, help_text='A 3 Letter (usually) identifier for the cryptocurrency, e.g. BTC or ETH')
  name = models.CharField(max_length=50, unique=True, help_text='The full name of the cryptocurrency')


class FiatCurrency(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  symbol = models.CharField(max_length=5, unique=True)
  name = models.CharField(max_length=20, unique=True)


class PriceRecord(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  # Both From and To fields can be Crypto or Fiat
  # -> made them generic with content_types
  # From field is used as base
  from_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='from_price_records')
  from_id = models.UUIDField()
  from_object = GenericForeignKey('from_type', 'from_id')
  from_amount = models.FloatField(blank=False, null=False)
  to_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='to_price_records')
  to_id = models.UUIDField()
  to_object = GenericForeignKey('to_type', 'to_id')
  created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
  updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
  