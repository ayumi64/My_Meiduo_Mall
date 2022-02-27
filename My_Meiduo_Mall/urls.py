from django.conf.urls import url
from . import views


urlpatterns = [
    # 验证码图片的路径
    # this.host + "/image_codes/" + this.image_code_id + "/"
    # /image_codes/f117ebe5-34d1-4ff8-852d-e1342a65581e/
    url(r'^image_codes/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view()),

    # 匹配手机验证的路径
    # this.host + '/sms_codes/' + this.mobile +
    # '/?image_code=' + this.image_code
    url(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SmsCodeView.as_view()),



]
