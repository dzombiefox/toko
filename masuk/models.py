# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from suplier .models import Suplier

# Create your models here.
class Masuk(models.Model):
    methode = (
        ('0', 'HUTANG'),
        ('1', 'LUNAS'),

    )
    tanggal=models.DateField(verbose_name="TANGGAL")
    nota=models.CharField(max_length=15,verbose_name="NO NOTA")
    suplier=models.ForeignKey(Suplier,verbose_name="SUPLIER")
    sales=models.CharField(max_length=50,verbose_name="NAMA SALES")
    pembayaran=models.CharField(max_length=6,choices=methode,default='1')
    jangkaWaktu=models.CharField(max_length=250,verbose_name="JANGKA WAKTU")
    status=models.CharField(max_length=15,blank=True)
    keterangan=models.TextField(null=True)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.nota

    def encoded_id(self):
        from Crypto.Cipher import AES
        import base64
        MASTER_KEY = "Some-long-base-key-to-use-as-encyrption-key"
        enc_secret = AES.new(MASTER_KEY[:32])
        tag_string = (str(self.id) +
                      (AES.block_size -
                       len(str(self.id)) % AES.block_size) * "\0")
        cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))
        return cipher_text


    def decode_id(self,id):
        return id


            # from Crypto.Cipher import AES
            # import base64
            # MASTER_KEY = "Some-long-base-key-to-use-as-encyrption-key"
            # dec_secret = AES.new(MASTER_KEY[:32])
            # raw_decrypted = dec_secret.decrypt(base64.b64decode(id))
            # clear_val = raw_decrypted.rstrip("\0")
            # return clear_val
    #
    # def decoded_id(cipher_text):
    #     from Crypto.Cipher import AES
    #     import base64
    #     MASTER_KEY = "Some-long-base-key-to-use-as-encyrption-key"
    #     dec_secret = AES.new(MASTER_KEY[:32])
    #     raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text))
    #     clear_val = raw_decrypted.rstrip("\0")
    #     return clear_val
