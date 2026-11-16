# Python intro — ćwiczenia samodzielne

Pracuj w konsoli `python` lub `ipython`. Każde zadanie jest niezależne: wpisuj potrzebne polecenia samodzielnie, po jednym. Sprawdzaj wartości, wpisując nazwy zmiennych. Nie używaj pętli, instrukcji `if`, własnych funkcji ani bibliotek zewnętrznych. Dopuszczalne są poznane funkcje wbudowane i metody obiektów.

## 1. Operatory arytmetyczne — 10 zadań

**Zakres:** `+`, `-`, `*`, `/`, `//`, `%`, `**`, nawiasy. **Nie używaj zmiennych.**

1. **Czas nagrania.** Ile pełnych godzin i ile pozostałych minut mieści się w `367` minutach?
2. **Liczba pikseli.** Obraz ma `1024` kolumn i `768` wierszy. Ile zawiera pikseli?
3. **Rozmiar rastra.** Jednopasmowy obraz ma `1200 × 800` pikseli, a każdy piksel zajmuje `2` bajty. Ile zajmuje bajtów i MiB (`1 MiB = 1024²` bajtów)?
4. **Pakowanie zdjęć.** Archiwum zawiera `487` zdjęć. Na jednej płycie mieszczą się `24` zdjęcia. Ile pełnych płyt można nagrać i ile zdjęć pozostanie?
5. **Powierzchnia terenu.** Kwadratowy raster ma `4096 × 4096` pikseli, a rozmiar piksela wynosi `0.5` m. Jaką powierzchnię terenu obejmuje w hektarach (`1 ha = 10 000 m²`)?
6. **Zakres wartości.** Czujnik zapisuje pomiary jako liczby bez znaku na `12` bitach. Ile różnych wartości może zapisać i jaka jest największa wartość?
7. **Średni pomiar.** Pięć pomiarów opadu wynosi `12`, `19`, `11`, `17` i `21` mm. Jaki jest średni opad?
8. **Zmiana wielkości.** Po aktualizacji liczba wykrytych obiektów wzrosła z `80` do `92`. Jaki jest procentowy wzrost względem stanu początkowego?
9. **Odległość na mapie.** Na mapie w skali `1:25 000` odległość wynosi `7.6` cm. Ile to kilometrów w terenie?
10. **Godzina zakończenia.** Rejestracja rozpoczęła się o `22:45` i trwała `155` minut. O której godzinie się zakończyła? Podaj godzinę i minutę, uwzględniając przejście przez północ.

## 2. Zmienne i przypisania — 10 zadań

**Zakres:** zmienne, `=`, ponowne przypisanie, `+=`, `-=`, `*=`, obliczenia z użyciem nazw. Zapisuj dane i wyniki w czytelnie nazwanych zmiennych.

1. **Zmiana wymiarów obrazu.** Obraz ma początkowo `800 × 600` pikseli, a w nowej wersji `1200 × 900`. Oblicz liczbę pikseli obu wersji, korzystając z tych samych nazw wymiarów i tego samego wzoru.
2. **Rozdzielczość rastra.** Raster ma `650` kolumn, `400` wierszy i piksele o boku `10` m. Oblicz powierzchnię terenu w km². Jak zmieni się wynik, jeśli rozmiar piksela wzrośnie do `20` m?
3. **Zajętość dysku.** Na dysku jest już `250` GiB danych. W ciągu dnia zapisano kolejne `18` i `12` GiB, a następnie usunięto `5` GiB. Ile miejsca jest teraz zajęte?
4. **Budżet zakupów.** Laboratorium ma `3000` zł. Kamera kosztuje `640` zł, dysk `780` zł, a monitor `1150` zł. Ile pozostanie po zakupie wszystkich trzech urządzeń?
5. **Kalibracja czujnika.** Czujnik wskazuje `182.4` m, ale ma dodatni błąd systematyczny `1.8` m. Jaka jest wysokość po korekcie? Po ponownym wzorcowaniu błąd oszacowano na `1.2` m — przelicz wynik bez zmiany oryginalnego odczytu.
6. **Czas przejazdu.** Trasa ma `42` km. Oblicz czas jazdy w godzinach przy prędkości `56` km/h, a potem przy `70` km/h. Ile godzin uda się zaoszczędzić?
7. **Poprawka współrzędnych.** Punkt ma współrzędne `x = 423500` m i `y = 5547900` m. Poprawki wynoszą odpowiednio `+12.5` m i `-8` m. Oblicz współrzędne skorygowane; następnie zmień poprawkę `x` na `+13` m i zaktualizuj wynik.
8. **Plan poboru próbek.** W ciągu jednego dnia pobiera się `32` próbki. Ile próbek powstanie w `7` dni? A ile, jeśli czas kampanii skróci się do `5` dni?
9. **Wielopasmowy obraz.** Obraz ma `1000` kolumn, `800` wierszy, `3` pasma i `2` bajty na piksel każdego pasma. Oblicz jego rozmiar w MiB. Jak zmieni się wynik po dodaniu czwartego pasma?
10. **Nieaktualny wynik.** Dla kwadratowego pola o boku `35` m zapisz obliczoną powierzchnię w osobnej zmiennej. Po poprawieniu długości boku na `40` m sprawdź zapisaną powierzchnię i uzyskaj jej aktualną wartość.

## 3. Typy liczbowe i konwersje — 5 zadań

**Zakres:** `int`, `float`, `type()`, `int()`, `float()`, `round()`.

1. **Częstotliwość próbkowania.** Rejestrator zebrał `36` próbek w `8` sekund. Zapisz liczbę próbek i czas jako liczby całkowite, oblicz liczbę próbek na sekundę i sprawdź typ wyniku.
2. **Indeksy piksela.** Współrzędne w obrazie mają wartości `125.9` kolumny i `88.4` wiersza. Do odczytu piksela potrzebne są indeksy całkowite. Jakie indeksy otrzymasz po konwersji `int()` i jaka część każdej współrzędnej zostanie odrzucona?
3. **Korekta wysokości.** Wysokość zapisana jako liczba całkowita wynosi `275` m. Po uwzględnieniu poprawki `0.75` m powstaje wynik ułamkowy. Sprawdź typ oryginalnej wysokości, poprawki i wyniku.
4. **Wysokość w raporcie.** Pomiar wynosi `129.7` m. Raport wymaga pełnych metrów. Porównaj wynik konwersji `int()` z zaokrągleniem `round()` i sprawdź, co robi każda operacja.
5. **Dokładność dziesiętna.** Dwa odczyty wynoszą `0.1` i `0.2`. Oblicz ich sumę, sprawdź jej reprezentację w konsoli i zapisz wynik zaokrąglony do jednego miejsca po przecinku.

## 4. Porównania i wartości logiczne — 5 zadań

**Zakres:** `<`, `<=`, `>`, `>=`, `==`, `!=`, `and`, `or`, `not`. Zapisz wynik kontroli jako `True` albo `False`, bez używania `if`.

1. **Jakość obrazu.** Obraz ma `18%` zachmurzenia i rozdzielczość `10` m. Nadaje się do analizy, jeżeli zachmurzenie nie przekracza `20%` **i** rozdzielczość nie jest gorsza niż `10` m. Sprawdź, czy spełnia wymagania.
2. **Zakres czujnika.** Czujnik działa poprawnie w zakresie temperatur od `-40` do `60`°C, łącznie z granicami. Sprawdź, czy odczyt `-40`°C jest prawidłowy, i czy odczyt `61`°C też byłby prawidłowy.
3. **Poprawność pomiaru.** W systemie wartość `-9999` oznacza brak danych. Poprawny pomiar wilgotności musi być różny od tej wartości i mieścić się w zakresie `0–100%`. Sprawdź osobno odczyty `-9999` i `87`.
4. **Odrzucenie zdjęcia.** Zdjęcie odrzuca się, jeśli zachmurzenie przekracza `70%` **lub** kąt wychylenia kamery przekracza `30` stopni. Dla zachmurzenia `45%` i kąta `34` stopnie sprawdź, czy zdjęcie zostanie odrzucone i czy zostanie zaakceptowane.
5. **Wyjątek od reguły.** Do analizy dopuszcza się obraz, jeśli zachmurzenie nie przekracza `20%` i rozdzielczość nie przekracza `10` m. Obraz może być także dopuszczony na podstawie ręcznej zgody. Sprawdź wynik dla zachmurzenia `35%`, rozdzielczości `10` m i udzielonej zgody.

## 5. Łańcuchy znaków (`str`) — 10 zadań

**Zakres:** łączenie napisów, `str()`, indeksowanie, wycinki, `len()`, `in`, `strip()`, `lower()`, `replace()`, `count()`, `endswith()`.

1. **Nazwa sceny.** Identyfikator satelity to `S2A`, a data rejestracji to `20260715` (zapisana jako napis). Utwórz nazwę pliku `S2A_20260715.tif` z tych dwóch informacji.
2. **Niejednolity kod.** W bazie zapisano kod stacji jako `'  KrK-03  '`. Wymagany format to `krk-03` — bez spacji na brzegach i wyłącznie małymi literami.
3. **Plik maski.** Dla obrazu `scene_07.tif` potrzebna jest maska o nazwie `scene_07_mask.tif`. Utwórz nazwę maski na podstawie nazwy obrazu.
4. **Data z identyfikatora.** Nazwy plików mają stały format, np. `S2A_20260715_B04.tif`. Wydobądź z podanej nazwy ośmiocyfrową datę.
5. **Rozszerzenie pliku.** Do przetwarzania przyjmowane są wyłącznie pliki TIFF. Sprawdź, czy plik `DSM_5M.TIF` ma rozszerzenie `.tif`, niezależnie od wielkości liter.
6. **Etykieta stanowiska.** Kod regionu to `KRK`, a numer stanowiska jest liczbą całkowitą `12`. Utwórz napis `KRK-12`.
7. **Usunięcie przedrostka.** Program zapisał plik jako `raw_dem_10m.tif`. Wersja docelowa powinna mieć nazwę `dem_10m.tif`.
8. **Liczba wystąpień.** Wiersz raportu ma postać `cloud,cloud,clear,cloud`. Ile razy pojawia się w nim napis `cloud`?
9. **Kontrola identyfikatora.** Nazwa `S2A_20260715_B04.tif` powinna wskazywać satelitę `S2A` i pasmo `B04`. Sprawdź oba warunki za pomocą operacji na napisach.
10. **Długość kodu.** System przyjmuje identyfikatory o maksymalnej długości `20` znaków. Sprawdź, czy napis `S2A_20260715_B04` mieści się w limicie.

## 6. Listy (`list`) — 10 zadań

**Zakres:** lista elementów tego samego rodzaju, indeksy, wycinki, `append()`, `extend()`, `pop()`, `+`, `copy()`, `len()`, `sum()`, `min()`, `max()`, `sorted()`, `count()`, `in`.

1. **Seria temperatur.** W sześciu kolejnych godzinach zmierzono `15.2`, `13.8`, `16.1`, `14.0`, `15.7` i `16.4`°C. Przechowaj serię jako jeden obiekt i oblicz średnią bez ręcznego dodawania wszystkich elementów.
2. **Kolejna seria pomiarów.** Zapisane pomiary opadu to `[3, 0, 7, 2]` mm. Z kolejnej rejestracji otrzymano całą serię `[5, 4]` mm. Dołącz nową serię do istniejącej, zachowując dotychczasową listę jako główny rejestr pomiarów. Oblicz sumę opadu.
3. **Poprawienie błędnego pomiaru.** Seria temperatur wynosi `[12.1, 13.5, -9999, 14.2, 13.8]`. Trzeci odczyt poprawiono na `13.7`. Uzyskaj prawidłową serię i jej średnią.
4. **Usunięcie niepełnego odczytu.** Ostatni pomiar w serii `[7.2, 7.4, 7.3, -9999]` pochodzi z przerwanej rejestracji. Usuń go z serii i oblicz średnią pozostałych wartości.
5. **Zmienność pomiarów.** Wyniki jednej serii to `[21, 18, 26, 19, 24, 17]`. Znajdź najmniejszą i największą wartość oraz ich różnicę.
6. **Dobór pasm.** Dostępne pasma obrazu zapisano kolejno jako `['B02', 'B03', 'B04', 'B08', 'B11', 'B12']`. Potrzebny jest zestaw trzech pierwszych pasm widzialnych i dwóch ostatnich pasm SWIR, bez `B08`. Przygotuj listę wybranych pasm.
7. **Łączenie dni pomiarowych.** Pierwszego dnia zmierzono `[12.0, 13.0, 11.5]`, a drugiego `[14.0, 12.5]`. Potrzebna jest trzecia, wspólna seria w kolejności pomiarów. Obie listy dzienne muszą pozostać bez zmian, bo będą wykorzystane w osobnych raportach. Oblicz średnią dla wspólnej serii.
8. **Nowa próbka.** Dla pięciu próbek zapisano klasy `forest`, `water`, `forest`, `urban`, `forest`. Zarejestrowano jeszcze jedną próbkę klasy `forest`. Dopisz ją na końcu istniejącej listy. Sprawdź, czy występuje klasa `forest`, czy nie występuje `cloud`, oraz ile próbek ma klasę `forest`.
9. **Ranking błędów.** Liczby błędnych pikseli w pięciu próbkach wynoszą `[15, 3, 12, 8, 4]`. Przygotuj uporządkowane rosnąco wyniki do raportu, zachowując także oryginalną kolejność pomiarów.
10. **Dwa niezależne scenariusze.** Plan bazowy zakłada pobór `[10, 20, 30]` próbek w trzech miejscach. Plan alternatywny początkowo jest identyczny, ale w drugim miejscu przewidziano `25` próbek. Później w planie bazowym zwiększono liczbę próbek w pierwszym miejscu do `15`. Przechowaj oba plany tak, aby zmiana któregokolwiek nie wpływała na drugi.

## 7. Słowniki (`dict`) — 10 zadań

**Zakres:** opis obiektu za pomocą nazwanych pól; klucze i wartości, odczyt, aktualizacja, dodawanie, `get()`, `pop()`, `values()`, słowniki zagnieżdżone. **Zapisuj informacje o obiektach w słownikach, nie w niezależnych zmiennych o podobnych nazwach.**

1. **Metadane obrazu.** Obraz `S2A_01` ma `1000` kolumn, `800` wierszy i piksel o boku `10` m. Utwórz jeden rekord opisujący obraz i oblicz z niego powierzchnię w km².
2. **Opis stacji.** Stacja o kodzie `K01` znajduje się na wysokości `245` m i zmierzyła temperaturę `17.5`°C. Przechowaj jej dane w jednym rekordzie i utwórz etykietę `K01: 17.5 C`.
3. **Aktualizacja metadanych.** Rekord obrazu zawiera identyfikator `S2A_01` i datę `20260714`. Operator poprawił datę na `20260715` i podał zachmurzenie `12%`. Zaktualizuj ten sam rekord.
4. **Legenda klas.** W rastrze kody `1`, `2` i `3` oznaczają kolejno `water`, `forest` i `urban`. Utwórz legendę pozwalającą odczytać nazwę klasy na podstawie kodu. Odczytaj klasę `2` i dodaj kod `4` dla `agriculture`.
5. **Rozdzielczości pasm.** Rozdzielczości pasm `B02`, `B03`, `B04`, `B08` wynoszą `10` m, a pasma `B11` — `20` m. Zapisz powiązania kod–rozdzielczość tak, aby łatwo pobrać rozdzielczość `B11` i sprawdzić, czy istnieje wpis dla `B01`.
6. **Niepełny rekord.** Dla obrazu `S2A_02` zapisano tylko identyfikator i rok `2026`. Wyświetl wartość zachmurzenia, ale w przypadku braku tego pola uzyskaj napis `unknown`, bez błędu.
7. **Wyniki próbek.** Wartości pH dla próbek `P01`, `P02`, `P03` wynoszą odpowiednio `6.3`, `7.1`, `6.8`. Wynik `P02` poprawiono na `7.0`, a próbka `P04` ma pH `6.5`. Przechowaj wyniki według identyfikatorów i oblicz średnie pH.
8. **Usunięcie nieaktualnego pola.** Rekord danych ma pola: `id = S2A_01`, `format = tif`, `temporary_path = /tmp/image.tif`. Po przeniesieniu danych informacja o tymczasowej ścieżce nie powinna już znajdować się w rekordzie.
9. **Stacja z serią pomiarów.** Rekord stacji `K02` zawiera jednostkę `C` i serię temperatur `[14.0, 15.5, 15.0]`. Pojawił się odczyt `16.0`. Zachowaj serię wewnątrz rekordu i wyznacz jej średnią.
10. **Archiwum obrazów.** Archiwum zawiera dwa obrazy: `S2A_01` z zachmurzeniem `12%` i `S2A_02` z zachmurzeniem `35%`. Zorganizuj dane tak, aby po identyfikatorze obrazu można było odczytać jego metadane. Sprawdź, czy pierwszy obraz ma mniejsze zachmurzenie, i zapisz dla niego rozdzielczość `10` m.

## 8. Zadania łączące — 10 zadań

**Zakres:** wszystko z poprzednich części. Dobierz zmienne, listy i słowniki zgodnie z charakterem danych. Bez pętli, `if` i własnych funkcji.

1. **Parametry rastra.** Obraz `DEM_01` ma `1500 × 1000` pikseli o boku `5` m. Każdy piksel zajmuje `4` bajty. Przechowaj metadane jako jeden obiekt; oblicz powierzchnię terenu w km² oraz rozmiar pliku z surowymi pikselami w MiB.
2. **Wynik stacji.** Stacja `K01` zapisuje temperatury `[12.5, 13.0, 13.5]`°C. Po dopisaniu nowego pomiaru `14.0`°C raport powinien zawierać kod stacji i średnią temperaturę. Przygotuj dane i napis raportu.
3. **Nazwy powiązanych plików.** Metadane sceny zawierają satelitę `S2A` i datę `20260715`. Zapisz je w jednym rekordzie oraz wygeneruj powiązane nazwy obrazu `S2A_20260715.tif` i maski `S2A_20260715_mask.tif`.
4. **Próbki i legenda.** W próbkach zapisano kody klas `[1, 2, 2, 3, 2]`, a legenda to `1: water`, `2: forest`, `3: urban`. Ustal nazwę klasy `2` i policz, ile próbek należy do tej klasy.
5. **Kompozycja RGB.** Dostępne pliki pasm to `B02 → scene_B02.tif`, `B03 → scene_B03.tif`, `B04 → scene_B04.tif`. Kompozycja RGB używa kolejno `B04`, `B03`, `B02`. Przygotuj listę trzech nazw plików w kolejności R–G–B.
6. **Porównanie stacji.** Stacja `A` ma pomiary `[18, 20, 19]`°C, a stacja `B` — `[15, 17, 16]`°C. Umieść serie pod kodami stacji i oblicz różnicę ich średnich temperatur (`A − B`).
7. **Rejestr pomiarów.** Dwa kolejne pomiary mają identyfikatory `M01` i `M02` oraz wartości `15.2` i `16.4`. Drugi wynik skorygowano do `16.1`. Przechowaj pomiary w kolejności, każdy z własnym identyfikatorem, a następnie sprawdź, czy poprawiona wartość jest większa od pierwszej.
8. **Kolekcja obrazów.** W kolekcji są obrazy `S2A_01` (zachmurzenie `12%`) i `S2A_02` (`35%`). Dołącz obraz `S2A_03` (`8%`). Dane każdego obrazu powinny pozostać razem, a kolejność scen zachowana. Ustal liczbę obrazów i sprawdź, czy trzeci ma mniejsze zachmurzenie niż pierwszy.
9. **Zestawy obraz–maska.** Dla obrazu `A.tif` istnieje maska `A_mask.tif` z klasami `[1, 2]`, a dla `B.tif` maska `B_mask.tif` z klasami `[1, 3]`. Zapisz oba zestawy jako jedną kolekcję rekordów. Do drugiego zestawu dodaj klasę `4`, nie zmieniając pierwszego.
10. **Projekt klasyfikacji.** Projekt `landcover` zawiera dwa obrazy o identyfikatorach `S2A_01` i `S2A_02`, legendę `{1: 'water', 2: 'forest'}` oraz listę kodów próbek `[1, 2, 2, 1, 2]`. Umieść wszystkie informacje w jednej strukturze. Podaj nazwę klasy o kodzie `2`, liczbę jej próbek i identyfikator drugiego obrazu.
