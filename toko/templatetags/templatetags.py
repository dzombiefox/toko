from django import template
from bjual .models import Bjual
from jual .models import Jual
register = template.Library()

@register.filter(name='totalBelanja')
def totalBelanja(value):
    barangJual=Bjual.objects.filter(jual=value,pilihan=0)
    total = 0
    for data in barangJual:
        total +=int (data.hargaJual) * int (data.jumlahJual)
    return total

@register.filter(name='margin')
def margin(value):
    barangJual = Bjual.objects.filter(jual=value, pilihan=0)
    tot = 0
    for data in barangJual:
        # return int(self.jumlahJual) * (int(self.hargaJual) - (int(self.hargaModal)))
        tot += int(data.jumlahJual)*(int(data.hargaJual) - int(data.hargaModal))
    return tot

@register.filter(name='potonganbonus')
def potonganbonus(value):
    barangJual = Bjual.objects.filter(jual=value, pilihan=1)
    totalbonus = 0
    for data in barangJual:
        totalbonus += int(data.hargaModal) * int(data.jumlahJual)
    return totalbonus


@register.filter(name='totalkeuntungan')
def totalkeuntungan(value):
    data=Jual.objects.get(pk=value)
    diskon=data.potongan
    pbonus=potonganbonus(value)
    mar=margin(value)
    hasil = int(mar) - int(diskon) - int(pbonus)
    return hasil

@register.filter(name="rangekeuntungan")
def rangekeuntungan(date1,date2):
    # return 17
    jual = Jual.objects.filter(tanggal__range=(date1,date2))
    totalall = 0
    for data in jual :
         diskon = data.potongan
         pbonus = potonganbonus(data.id)
         mar = margin(data.id)
         hasil = int(mar) - int(diskon) - int(pbonus)
         totalall+=hasil
    return totalall



    # mar = margin(value)
    # hasil = int(mar) - int(diskon) - int(pbonus)
    # return hasil

@register.filter(name="omset")
def rangeomset(date1,date2):
    jual = Jual.objects.filter(tanggal__range=(date1, date2))
    totalall = 0
    for data in jual :
        bjual = Bjual.objects.filter(jual=data.id,pilihan=0)
        for databjual in bjual:
            totalall += int(databjual.hargaJual)* int (databjual.jumlahJual)

    return totalall


@register.filter(name="encode_id")
def encoded_id(value):
        from Crypto.Cipher import AES
        import base64
        MASTER_KEY = "Some-long-base-key-to-use-as-encyrption-key"
        enc_secret = AES.new(MASTER_KEY[:32])
        tag_string = (str(value) +
                      (AES.block_size -
                       len(str(value)) % AES.block_size) * "\0")
        cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))
        return cipher_text
