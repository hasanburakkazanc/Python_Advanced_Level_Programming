# 1 den yüze kadar olan bütün sayıları listenin içine ekle 100 de dahil

my_list =[]

for x in range (1,101):
    my_list.append(x)

    print(my_list)


#formüül = [ değişken adı for değişken_adı in range (1,101)]

my_list1_comp = [x for x in range(1,101)]
print(my_list1_comp)




#1 den 100 e kadar olan sayılar arasında 2 ye tam bölünen  sayıları ekleyen kodu yazın
#1. yol
my_list2 =[]

for i in range (2,101,2):
    my_list2.append(i)

#1. yol

my_list2_comp = []

for i in range (1,101):
    if i%2 == 0:
        my_list2_comp.append(i)
    else : pass





# list comperhenstion ile yapımı
my_list3 =[]
my_list3 = [x for x in range(1,101) if x%2 ==0]
print(my_list3)










# list ile 1 den 100 e kadar olan her sayının 3 katını yazan kodu yazınız

my_list4 = []

my_list4 = [x*3 for x in range(1,101)]
print(my_list4)

#list comp formülü
#[değişken adı ve yapılacak işlem for deüişken_adı in range(baişnagıç,bitiş)]




my_word_list = ["Furkan","Atlan","ybs","ztyoo","ybs-3b"]
#bu listenin tüm elemanlarının büyük karakterlele yazdırıp yeni bir listeye ekleyen kodu yazonoz

my_word_list_comp =[x.upper() for x in my_word_list]


#aynı kelime listesindeki a harflerini e harfi olarak değiştirip yeni bir listeye ekleyin list comphernstion ile yapın


my_word_list = ["Furkan","Atlan","ybs","ztyoo","ybs-3b"]

my_word_list2_comp = [x.replace("a","e") for x in my_word_list ]
print(my_word_list2_comp )




# 1 den 100 ekadar olan sayılar içirerisnde tek sayıları negatife dönüştüren çift sayılarında karesini alan  ve bunlar yen bir listeye ekleten kod

gecici_list = []

for  x in range(1,101):
    if x%2 == 0:
        gecici_list.append(x**2)
        
    else:
        gecici_list.append(-x)


print(gecici_list)

#list comp ile yapımı if else yapısı
# formül [ x_if_hali if x _şart else x_else_hali  for x in  liste]
sayi_list_comp = [-x if x%2!=0 else x**2 for x in range(1,101)]
print(sayi_list_comp)



# 1 den 100 e kadar olan tek sayılarda " tek"
# çift sayılarda "çift" yazan kodu yazınız
#hem normal kod hem de list comp ile (listeye eklemek)


benim_list =[]
for i in range(1,101):
    if i%2!= 0:
        benim_list.append("tek")
    else:
        benim_list.append("çift")


cift_tek_comp =["tek" if x%2!=0 else"çift" for x in range(1,101) ]
print(cift_tek_comp)




# 1 den 5 kadar olan listenin değeri ile 6 ten 10 a kadar olan listenin değerini çarpan kod 5 ,10 dahil


liste_3 = []
for i in range(1,6):
    for x in range(6,11):
        print(f"i = {i}")
        liste_3.append(x*i)
  



print(liste_3)


my_list5_comp = [a*b for a in range(1,6 ) for b in range(6,11)]



notlar ={"ahmet":65,"ali":78,"yusuf":15,"tuğçe":40,"kaan":50}

#notları 50 den büyük olan öğrencilerim isimleerimi getiren kodu yazon

#dictionary.items() fonksiyonu sırasıyla key ve valuer değerlerini döndürür
#dolayısıyla bu fonksiyonu kullanıp ili değişken atamsı yapıtoyuz
for my_key, my_value in notlar.items():
    if my_value >50:
        print(my_key)


list_dict_comp =[key for key,value in notlar.items() if value>50]
print(list_dict_comp)

