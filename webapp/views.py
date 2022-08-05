import logging
import traceback

from django.shortcuts import render
from django.http import JsonResponse

logger = logging.getLogger("root")


def home_page(request):
    return render(request, "index.html")


def test(request):
    """
    用于后台动态请求测试
    """
    ret = {"result": False, "data": [], "message": ""}

    try:
        flag = request.GET.get("flag", "")
        ret["result"] = True
        ret["data"].append({"flag": flag})
    except (KeyError, ValueError, IndexError, TypeError, AttributeError, Exception) as _:
        logger.error(traceback.format_exc())
        ret["message"] = traceback.format_exc()

    return JsonResponse(ret)
