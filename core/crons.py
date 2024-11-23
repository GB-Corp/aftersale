from datetime import timedelta

from django.utils import timezone
from drf_api_logger.models import APILogsModel

from api.models import WebServiceLog


def purge_logs():
    print(f'{timezone.now()} Purge logs start...')
    thirty_days_ago = timezone.now() - timedelta(days=7)
    WebServiceLog.objects.filter(created_on__lt=thirty_days_ago).delete()
    APILogsModel.objects.filter(added_on__lt=thirty_days_ago).delete()
    print(f'{timezone.now()} Purge logs end.')
