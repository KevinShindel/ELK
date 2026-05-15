import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def root(request):
    logger.error(msg="test message")
    return HttpResponse(content=b"http content", content_type="text/html")
