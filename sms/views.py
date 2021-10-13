from django.core.exceptions import SuspiciousOperation
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import logging

logger = logging.getLogger(__name__)


@require_POST
def send(request: HttpRequest):
    data = request.data
    print(data)
    response_data = {"status": "success"}
    return JsonResponse(response_data, 200)
