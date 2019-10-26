import matplotlib.pyplot as plt
import math
import urllib.request
from bs4 import BeautifulSoup
import locale
import statistics
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}


def tic():
    # Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()


def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print("Toc: start time not set")

class Regrasyon():
    matris1 =[0]
    matris2 = []
    matris3 =[]
    mSize = -1
    kareMatrisBoyut = -1
    sonucMatris = []
    def __init__(self, a, b,degree):
        self.a = a
        self.b = b
        self.degree = degree
        self.mSize = len(b)
        self.kareMatrisBoyut = (self.degree+1) * (self.degree+1) - 1
        self.matris1 = [0]
        for i in range(self.kareMatrisBoyut):
            self.matris1.append(0)
        self.matrisHesapla()
    def yazdir(self):
         #print(self.matris1)
        a = ""


    def matrisHesapla(self):
        self.matris1[0] = self.mSize;
        for i in range(1,self.kareMatrisBoyut+1):
            for k in range(self.mSize):
                self.matris1[i] = self.matris1[i]+pow(self.a[k],(i))

        self.matrisOlustur()

    def matrisOlustur(self):
        self.matris2= []
        for i in range(self.degree+1):
            matrisx= []
            for k in range(i,self.degree+i+1):
                matrisx.append(self.matris1[k])
            self.matris2.append(matrisx)

        self.matris3Olustur()

    def matris3Olustur(self):
        self.matris3=[]
        for i in range((self.degree+1)):
            toplam=0
            for k in range(self.mSize):
                toplam += self.b[k]*pow(self.a[k],i)
            self.matris3.append(toplam)

        self.sonucMatris = sonuc(self.matris2,self.matris3)


    def tahminEt(self,x):
        toplam = 0

        for i in range(len(self.sonucMatris)):
            toplam += self.sonucMatris[i] * pow(x, i)

        return  toplam

def sonuc(matrisA,matrisB):


    boyut = len(matrisA)
    for i in range(boyut):
        k = 1;
        for j in range(i+1,boyut):
            if matrisA[j-k][i] != 0:
                fark = (matrisA[j][i]) / (matrisA[(j-k)][i]);

                for sutun in range(boyut):
                    matrisA[j][sutun] = matrisA[j][sutun] -(fark*matrisA[j-k][sutun]);
                matrisB[j] = matrisB[j]  -(fark* matrisB[j-k])
                k = k+1;


    for i in range(boyut):
        if matrisA[i][i] != 1:
            payda = matrisA[i][i]
            matrisB[i] = matrisB[i] / payda
            for sutun in range(boyut):
                matrisA[i][sutun] = matrisA[i][sutun] / payda


    i = boyut-1
    while i>=0:
        matrisB[i] = matrisB[i] / matrisA[i][i];
        j=(i-1)
        while j>=0:
            matrisB[j] = matrisB[j] - matrisA[j][i] * matrisB[i]
            matrisA[j][i] = 0;
            j -= 1
        i -=1
    return matrisB

def yeniDeger(matrisA,d):
    y = []
    for i in range(len(matrisA)):
        y.append(d.tahminEt(matrisA[i]))
    return y

    # def yazdır(x,y,d):
    #
    #   newY = yeniDeger(x,d)
    #   toplamHata = 0
    #  boy = len(y)
    # for eleman in range(boy):
    #    adim=0
    #   adimOrani = 0.1
    #  while adim<=1:
    #     """Toplam hatanın toplamını 2 şekilde bulabiliriz. 1-Adımın durumuna göre sağ ve soldaki elemana göre farkı alırız. 2-sadece küçük elemana göre fark alırız"""
    #   if adim>=0.5 and (eleman+1)!=boy:
    #      deger = pow(d.tahminEt(x[eleman] + adim),2);
    #   fark = math.fabs(pow(y[eleman+1],2) -deger )
    toplamHata += math.sqrt(fark)

    # else:
    #   fark =math.fabs(pow( y[eleman],2)-pow(d.tahminEt(x[eleman]+adim),2))
    #   toplamHata += math.sqrt(fark)

    # """fark = (y[eleman]-d.tahminEt(x[eleman]+adim))
    # toplamHata += math.fabs(pow(fark, 2))"""
    # adim += adimOrani
    # """Toplam hatayı son olarak 3 sekilde hesap edebiliriz. 1-toplam hatayı işlem yapadan alabiliriz. 2-karekökünü alabiliriz. 3-10'a bölüp karakökükü alabiliriz"""
    # toplamHata = toplamHata/((1/adimOrani)*boy)
    # toplamHata = math.sqrt(toplamHata)

    # return x,y,newY,toplamHata


def yazdır(x,y,d):

    newY = yeniDeger(x,d)
    toplamHata = 0
    boy = len(y)
    for eleman in range(boy):
        adim=0
        adimOrani = 0.1
        while adim<=1:
            """Toplam hatanın toplamını 2 şekilde bulabiliriz. 1-Adımın durumuna göre sağ ve soldaki elemana göre farkı alırız. 2-sadece küçük elemana göre fark alırız"""
            if adim>=0.5 and (eleman+1)!=boy:
                fark = y[eleman+1] - d.tahminEt(x[eleman] + adim)
                toplamHata += pow(fark, 2)
            else:
                fark = y[eleman]-d.tahminEt(x[eleman]+adim)
                toplamHata += pow(fark,2)

            """fark = (y[eleman]-d.tahminEt(x[eleman]+adim))
            toplamHata += math.fabs(pow(fark, 2))"""
            adim += adimOrani
    """Toplam hatayı son olarak 3 sekilde hesap edebiliriz. 1-toplam hatayı işlem yapadan alabiliriz. 2-karekökünü alabiliriz. 3-10'a bölüp karakökükü alabiliriz"""
    toplamHata = math.sqrt(toplamHata/(1/adimOrani))
    #toplamHata = math.sqrt(toplamHata)

    return x,y,newY,toplamHata

def gurultuTemizle(a,b):
    x = a.copy();
    y = b.copy();
    """x = []#bilr algoritma denedim çalışmadı daha sorna bakabilirim.
    for i in range (len(a)):
        x.append(min(a[i:len(a)]));
    print(x)"""
    boyut=len(x)
    for i in range(boyut-1):
        for k in range(boyut - 1):
            if(y[k]>y[k+1]):
                temp = y[k]
                temp2 = x[k]
                y[k]= y[k+1]
                y[k+1]=temp
                x[k] = x[k+1]
                x[k+1] = temp2

    bolum = round(len(x)/4);

    irq = math.fabs(y[bolum*3]-y[bolum])
    altSinir = y[bolum]-(irq*0.5)
    ustSinir = y[3*bolum]+(irq*0.5)
    boyut= len(x)
    silinecek = []
    say = 0
    for i in range(boyut):
        if y[i]<altSinir or y[i]>ustSinir:
            silinecek.append(i-say)
            say+=1
    boyut = len(silinecek)
    print("temizle altsınır ve ust sınır:",altSinir,ustSinir)
    for i in range(boyut):
        y.pop(silinecek[i])
        x.pop(silinecek[i])

    boyut = len(x)
    #f = []

    for i in range(boyut - 1):
        for k in range(boyut - 1):
            if (x[k] > x[k + 1]):
                temp = x[k]
                temp2 = y[k]
                x[k] = x[k + 1]
                x[k + 1] = temp
                y[k] = y[k + 1]
                y[k + 1] = temp2
        #f.append(i + 1)
    #f.append(boyut)
    return x,y

def basariTesti(x,y,kabulEdilenHata):
    uzunluk = len(x)
    testBaslangic = round(uzunluk*0.15)
    if(testBaslangic<4):
        testBaslangic=4
    yeniX= x[testBaslangic:uzunluk-1]
    yeniY = y[testBaslangic:uzunluk-1]
    yeniUzunluk = len(yeniX)
    dogruSayisi = 0
    enKucukHata = 999999
    enKucukHataDerece = 0

    for f in range(yeniUzunluk+1):
        enKucukHata = 999999
        enKucukHataDerece = 0
        for i in range(1, 15):
            d = Regrasyon(x[f:testBaslangic+f], y[f:testBaslangic+f], i)
            d.yazdir()
            ax, ay, newY, toplamHata = yazdır(x[f:testBaslangic+f], y[f:testBaslangic+f], d)

            if (abs(enKucukHata) > abs(toplamHata)):
                enKucukHata = toplamHata
                enKucukHataDerece = i


        d2= Regrasyon(ax, ay, enKucukHataDerece)
        d2.yazdir()
        tahminci = (x[testBaslangic+f])
        tahmin = d2.tahminEt(tahminci)
        print("---------------------------")
        print("x eğitim matrisi:",ax)
        print("y sonuc matirisi:",ay)
        print("tahmin derecesi: ",enKucukHataDerece)
        print("tahmin edilecek x:",tahminci)
        print("tahminimiz:",tahmin,y[testBaslangic+f])

        if(tahmin<= y[testBaslangic+f]+kabulEdilenHata and tahmin >=y[testBaslangic+f]-kabulEdilenHata):
            print("dogru")
            dogruSayisi = dogruSayisi+1
        print(uzunluk-testBaslangic,"/",dogruSayisi,"-",dogruSayisi/(f+1),"(",dogruSayisi,"/",(f+1),")")
if __name__ == '__main__':
    tic()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    c = [5, 15, 16, 28, 45, 54, 56, 80, 97]
    usd =  [5.5518, 5.4296, 5.4322, 5.3134, 5.3560, 5.3612, 5.4583, 5.4606, 5.4621, 5.4685, 5.4776, 5.4624, 5.3481, 5.3318, 5.3398, 5.3075, 5.3776, 5.3080, 5.2960, 5.2875, 5.2976, 5.2477, 5.2716, 5.2219, 5.1631]
    euro = [6.2892, 6.1827, 6.1949, 6.0605, 6.1209, 6.1258, 6.2055, 6.1902, 6.1893, 6.1346, 6.1848, 6.1780, 6.0583, 6.0889, 6.0959, 6.0786, 6.1148, 6.0432, 6.0416, 5.9968, 6.0076, 5.9446, 5.9508, 5.9355, 5.8823]
    euroused = [1.1176 , 1.1202, 1.1205, 1.1224, 1.1241,1.1215,1.1194,1.1189	, 1.1198,1.1173, 1.1178, 1.1202, 1.1215, 1.1185, 1.1153, 1.1130, 1.1160, 1.1229, 1.1259, 1.1246, 1.1240	, 1.1297 ]
    """günleri 2 şekilde alabiliriz. 1-veri birden başlayarak veri uzunluğuna göre alabiliriz. 2-ayın günlerine göre alabiliriz"""
    days1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    days2 = [1,2,4,5,6,7,8,9,11,12,13,14,15,16,18,19,20, 21, 22, 23,  25, 26, 27, 28,29]
    eudays1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    onlineKur = []
    onlineDays = []
    r = urllib.request.Request('http://paracevirici.com/doviz-arsiv/merkez-bankasi/gecmis-tarihli-doviz/2018/amerikan-dolari', headers=headers)
    x = urllib.request.urlopen(r)
    source = BeautifulSoup(x, "html.parser")
    a = source.find_all("div", attrs={"class": "row"})

    daySay = 1;
    for k in source.find_all("p", attrs={"class": "price sell"})[1:]:
        onlineKur.append(float(k.text[:-2].replace(',','.')))
        onlineDays.append(daySay)
        daySay+=1

    r = urllib.request.Request(
        'http://paracevirici.com/doviz-arsiv/merkez-bankasi/gecmis-tarihli-doviz/2019/amerikan-dolari', headers=headers)
    x = urllib.request.urlopen(r)
    source = BeautifulSoup(x, "html.parser")
    a = source.find_all("div", attrs={"class": "row"})

    for k in source.find_all("p", attrs={"class": "price sell"})[1:]:
        onlineKur.append(float(k.text[:-2].replace(',', '.')))
        onlineDays.append(daySay)
        daySay += 1

    testX = onlineDays
    testY = onlineKur
    testX,testY = gurultuTemizle(testX,testY)
    print(testY)
    print(testX)
    deg = 15

    baslangicDerece = 1
    sonDerece = deg
    enKucukHata = 999999
    enKucukHataDerece = 0


    plt.figure(1)
    for i in range(baslangicDerece,sonDerece):
        d = Regrasyon(testX, testY, i)
        d.yazdir()
        x, y, newY, toplamHata= yazdır(testX, testY, d)

        if i == baslangicDerece:
            plt.scatter(x, y, label='Gercek Deger')
        #plt.subplot(derece, 1, i)
        #plt.plot(x, newY, 'o-',label=(i,'-',toplamHata))
        plt.plot(x, newY, label=(i, '-', toplamHata))
        plt.xlabel("GÜN")
        plt.ylabel("TL")

        plt.legend()
        if(abs(enKucukHata) > abs(toplamHata)):
            enKucukHata = toplamHata
            enKucukHataDerece = i
        # plt.subplot(2, 1, 2)
        # plt.scatter(x, y,label="Gercek")
        # plt.plot(x, newY,label="Tahmin")
        # plt.legend()


    plt.figure(2)
    d = Regrasyon(testX, testY, enKucukHataDerece)
    d.yazdir()
    x, y, newY, toplamHata = yazdır(testX, testY,d)
    plt.scatter(x, y,c='r' ,label='Gercek Deger')
    plt.plot(x, newY, 'o-', label=(enKucukHataDerece, '-', toplamHata))
    plt.legend()
    plt.xlabel("GÜN")
    plt.ylabel("TL")

    tahminci = len(testX)+1
    print(tahminci)
    print(("tahmin: ", d.tahminEt(tahminci)))
    toc()

    #kabulEdilenHata = ((max(testY)-min(testY))/len(testY))*10
    #kabulEdilenHata = statistics.stdev(testY)
    #print(kabulEdilenHata)
    #basariTesti(testX, testY,kabulEdilenHata)
    plt.show()


