from django.db import models
from base.models import *
from dangkyhoc.models import *
# Create your models here.

class KetQuaHocTap(BaseModel):
    ID=models.AutoField(primary_key=True)
    MaSinhVien=models.ForeignKey(SinhVien,on_delete=models.CASCADE)
    MaMon=models.ForeignKey(MonHoc,on_delete=models.SET_NULL,null=True)
    DiemQuaTrinh=models.FloatField(null=True,blank=True)
    DiemThi=models.FloatField(blank=True,null=True)
    DiemTongKet=models.FloatField(blank=True,null=True)
    DiemChu=models.CharField(max_length=100,blank=True,null=True)
    HocKy=models.IntegerField(blank=True,null=True)
    NamHoc=models.CharField(max_length=10,blank=True,null=True)
    DiemKN1=models.FloatField(blank=True,null=True,default=0)
    DiemKN2=models.FloatField(blank=True,null=True,default=0)
    DiemKN3=models.FloatField(blank=True,null=True,default=0)
    DiemKN4=models.FloatField(blank=True,null=True,default=0)
    TongKetKN1=models.FloatField(blank=True,null=True,default=0)
    TongKetKN2=models.FloatField(blank=True,null=True,default=0)
    TongKetKN3=models.FloatField(blank=True,null=True,default=0)
    TongKetKN4=models.FloatField(blank=True,null=True,default=0)
    Status=models.CharField(max_length=20,default='Chưa qua')
    DiemThiLai1=models.FloatField(blank=True,null=True,default=0)
    DiemThiLai2=models.FloatField(blank=True,null=True,default=0)
    DiemThiLai3=models.FloatField(blank=True,null=True,default=0)
    DiemThiLai4=models.FloatField(blank=True,null=True,default=0)
    DiemThiLai=models.FloatField(blank=True,null=True)

    class Meta:
        verbose_name='Kết quả học tập'
        verbose_name_plural='Kết quả học tập'

class HeSoMonHoc(BaseModel):
    ID=models.AutoField(primary_key=True)
    MaMon=models.ForeignKey(MonHoc,on_delete=models.CASCADE)
    HeSoDiemQuaTrinh=models.FloatField()
    HeSoTongKet=models.FloatField()
    HeSoKN1=models.FloatField()
    HeSoKN2=models.FloatField()
    HeSoKN3=models.FloatField()
    HeSoKN4=models.FloatField()
    HeSoTongKetKN1=models.FloatField()
    HeSoTongKetKN2=models.FloatField()
    HeSoTongKetKN3=models.FloatField()
    HeSoTongKetKN4=models.FloatField()
    HeSoTongKet=models.FloatField()
    HeSoDiemThiLai=models.FloatField()

    class Meta:
        verbose_name='Hệ số môn học'
        verbose_name_plural='Hệ số môn học'