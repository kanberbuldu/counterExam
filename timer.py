import time
try:
    counter = int(input("Geri Sayım Kaçtan Başlasın: "))
    print("Geri sayım Başlıyor !")
    time.sleep(2)
    while counter > 0:
        print(f"{counter}", end="")
        time.sleep(1)
        counter -= 1
        print("\r",end="")
    print("Time is up! ")

except:
    print("Lütfen Sayı girdiğinize emin olun!")



