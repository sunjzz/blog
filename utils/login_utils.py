# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/27 14:45
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequired(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequired, self).dispatch(request, *args, **kwargs)