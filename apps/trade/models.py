from django.db import models
from django.contrib.auth.models import User

TRADE_TYPE = (
    ("BUY", "BUY"),
    ("SELL", "SELL"),
)


class Symbol(models.Model):
    symbol_name = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol_name


class Journal(models.Model):
    trader = models.ForeignKey(User, related_name='trader', on_delete=models.CASCADE, verbose_name='Trader')
    symbol_name = models.ForeignKey(Symbol, related_name='journal', on_delete=models.DO_NOTHING, verbose_name='Cặp tiền')
    pre_analysis = models.TextField(max_length=500, verbose_name='Phân tích tổng thể')
    upcoming_event = models.CharField(max_length=100, verbose_name='Lịch Kinh tế', blank=True, null=True)

    trade_note = models.TextField(max_length=500, verbose_name='Đánh giá điểm trade', blank=True, null=True)
    htf_image = models.ImageField(upload_to="static/upload/images/", blank=True, null=True)
    ttf_image = models.ImageField(upload_to="static/upload/images/", blank=True, null=True)
    ltf_image = models.ImageField(upload_to="static/upload/images/", blank=True, null=True)
    entry_type = models.CharField(max_length=10, choices=TRADE_TYPE, verbose_name='Loại')
    entry_time = models.DateTimeField(verbose_name='Giờ mở lệnh', blank=True, null=True)
    entry_price = models.FloatField(default=0, verbose_name='Giá mở lệnh')
    entry_sl = models.FloatField(default=0, verbose_name='Giá SL')
    entry_tp = models.FloatField(default=0, verbose_name='giá TP')

    during_trade_analysis = models.TextField(max_length=2000,verbose_name='Phân tích trong khi trade', blank=True, null=True)

    closed_price = models.FloatField(default=0, verbose_name='Giá đóng lệnh', blank=True, null=True)
    closed_time = models.DateTimeField(verbose_name='Giờ đóng lệnh', blank=True, null=True)
    trade_image = models.ImageField(upload_to="static/upload/images/", blank=True, null=True)
    post_analysis = models.TextField(max_length=500, verbose_name='Phân tích sau trade', blank=True, null=True)

    # created_by = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    # updated_by = models.ForeignKey(User, related_name='updater', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Journal'

    def __str__(self):
        return self.symbol_name
