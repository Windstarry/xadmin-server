#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : xadmin-server
# filename : verify
# author : ly_13
# date : 8/7/2024

from common.utils import get_logger
from settings.serializers.verify import VerifyCodeSettingSerializer, CaptchaSettingSerializer
from settings.views.settings import BaseSettingViewSet

logger = get_logger(__name__)


class VerifyCodeSettingViewSet(BaseSettingViewSet):
    """验证码规则"""
    serializer_class = VerifyCodeSettingSerializer
    category = "verify"


class CaptchaSettingViewSet(BaseSettingViewSet):
    """图片验证码"""
    serializer_class = CaptchaSettingSerializer
    category = "captcha"
