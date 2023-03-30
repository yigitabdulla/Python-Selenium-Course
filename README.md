# Python-Selenium-Course
Pytest'te dekoratörler, testlerin veya test fonksiyonlarının davranışını değiştirmek için kullanılır. Pytest'te yaygın olarak kullanılan dekoratörlerden bazıları:

@pytest.fixture: Bu dekoratör, işlevleri test etmek için yeniden kullanılabilir veriler veya kaynaklar sağlayan işlevler olan fikstürleri tanımlamak için kullanılır.
Fikstürler, diğer şeylerin yanı sıra test verilerini ayarlamak, nesneleri başlatmak veya veritabanlarına bağlanmak için kullanılabilir.

@pytest.mark.parametrize: Bu dekoratör, tek bir test işlevi için birden çok giriş verisi kümesi tanımlamak için kullanılır.
Bu, yazmanız ve korumanız gereken kod miktarını azaltarak, farklı giriş değerleriyle çalıştırılabilen tek bir test işlevi yazmanıza olanak tanır.

@pytest.mark.skip: Bu dekoratör, bir test işlevini atlamak için kullanılır.
Test çalıştırıldığında görüntülenecek olan testi atlamak için bir neden sağlayabilirsiniz.

@pytest.mark.xfail: Bu dekoratör, bir testi başarısız olması beklendiği gibi işaretlemek için kullanılır.
Bu, kodunuzda izlemek istediğiniz bilinen bir sorun olduğunda, ancak test takımında başarısız olmak istemediğinizde kullanışlıdır.
