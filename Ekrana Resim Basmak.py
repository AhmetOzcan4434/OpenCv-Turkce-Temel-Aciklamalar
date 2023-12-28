# OpenCV kütüphanesini ekleyin
import cv2

# Dosya_Yolu değişkenine resmin dosya yolunu atayın
Dosya_Yolu = "resminizin_yolu.jpg"  

# cv2.imread fonksiyonuyla resmi okuyun
resim = cv2.imread(Dosya_Yolu)

# cv2.imshow fonksiyonuyla resmi ekranda gösterin
cv2.imshow("Ornek Resim", resim)
# İlk parametre, pencerenin adını temsil eder.
# İkinci parametre, görüntüyü temsil eder.

# cv2.waitKey fonksiyonu kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)
# 0 parametresi, kullanıcı bir tuşa basana kadar beklemeyi sağlar.
# Diğer bir sayı kullanıldığında, o kadar milisaniye boyunca bekler.

# cv2.destroyAllWindows fonksiyonu tüm pencereleri kapatır
cv2.destroyAllWindows()
# Bu fonksiyon, tüm OpenCV pencerelerini kapatmak için kullanılır.
# Eğer yalnızca belirli bir pencereyi kapatmak istiyorsanız, cv2.destroyWindow("Pencere_Adı") kullanabilirsiniz.
