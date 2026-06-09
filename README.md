# AI Gesture Controller

## Projekt zaliczeniowy z przedmiotu Metody sztucznej inteligencji

### Autor

Roman Panasiuk

### Opis projektu

AI Gesture Controller to aplikacja wykorzystująca techniki sztucznej inteligencji oraz widzenia komputerowego do sterowania funkcjami komputera za pomocą gestów dłoni wykonywanych przed kamerą internetową.

Program analizuje obraz z kamery w czasie rzeczywistym, rozpoznaje położenie dłoni, palców oraz twarzy użytkownika, a następnie wykonuje określone akcje systemowe lub efekty wizualne.

Projekt został wykonany w ramach przedmiotu **Metody sztucznej inteligencji**.

---

## Cel projektu

Celem projektu było zaprojektowanie i implementacja systemu sterowania komputerem za pomocą gestów dłoni z wykorzystaniem gotowych modeli sztucznej inteligencji.

Projekt demonstruje praktyczne zastosowanie:

* Computer Vision,
* Machine Learning,
* rozpoznawania gestów,
* segmentacji obrazu,
* śledzenia twarzy,
* przetwarzania obrazu w czasie rzeczywistym.

---

## Wykorzystane technologie

* Python 3.11
* OpenCV
* MediaPipe Tasks
* NumPy
* Windows API
* Kamera internetowa

---

## Funkcjonalności

Program obsługuje następujące gesty:

| Gest                                               | Akcja                   |
| -------------------------------------------------- | ----------------------- |
| Złączenie kciuka i palca wskazującego lewej dłoni  | Zwiększenie głośności   |
| Złączenie kciuka i palca wskazującego prawej dłoni | Zmniejszenie głośności  |
| Zaciśnięcie lewej dłoni w pięść                    | Włączenie maski klauna  |
| Zaciśnięcie prawej dłoni w pięść                   | Wyłączenie maski klauna |
| Zbliżenie obu dłoni do siebie                      | Włączenie rozmycia tła  |
| Oddalenie dłoni od siebie                          | Wyłączenie rozmycia tła |

---

## Zastosowane modele AI

Projekt wykorzystuje gotowe modele MediaPipe:

### Hand Landmarker

Model odpowiedzialny za:

* wykrywanie dłoni,
* śledzenie położenia dłoni,
* identyfikację 21 punktów charakterystycznych dłoni.

### Face Landmarker

Model odpowiedzialny za:

* wykrywanie twarzy,
* lokalizację punktów charakterystycznych twarzy.

### Selfie Segmenter

Model odpowiedzialny za:

* oddzielenie użytkownika od tła,
* generowanie maski segmentacyjnej,
* tworzenie efektu rozmycia tła.

---

## Struktura projektu

```text
AI-Gesture-Controller/
│
├── main.py
├── gesture_detector.py
├── volume_controller.py
├── face_effects.py
├── background_effects.py
├── requirements.txt
├── README.md
│
└── models/
    ├── hand_landmarker.task
    ├── face_landmarker.task
    └── selfie_segmenter.tflite
```

---

## Wymagania systemowe

### Sprzęt

* Kamera internetowa
* Minimum 8 GB RAM
* System Windows 10 lub Windows 11

### Oprogramowanie

* Python 3.11.x
* Git

---

## Instalacja projektu z GitHub

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/TWOJ_LOGIN/AI-Gesture-Controller.git
```

Przejście do katalogu projektu:

```bash
cd AI-Gesture-Controller
```

---

### 2. Utworzenie środowiska wirtualnego

```bash
py -3.11 -m venv .venv
```

---

### 3. Aktywacja środowiska

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Po poprawnej aktywacji powinien pojawić się prefiks:

```text
(.venv)
```

---

### 4. Instalacja bibliotek

```bash
pip install -r requirements.txt
```

---

### 5. Pobranie modeli AI

Utwórz katalog:

```bash
mkdir models
```

Następnie pobierz modele:

#### Hand Landmarker

https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task

#### Face Landmarker

https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task

#### Selfie Segmenter

https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_segmenter/float16/latest/selfie_segmenter.tflite

Po pobraniu umieść pliki w katalogu:

```text
models/
```

---

### 6. Uruchomienie programu

```bash
python main.py
```

---

## Zasada działania

1. Kamera przechwytuje obraz użytkownika.
2. Model Hand Landmarker wykrywa dłonie.
3. Program analizuje położenie palców.
4. Rozpoznawany jest odpowiedni gest.
5. Wykonywana jest przypisana akcja.
6. Face Landmarker śledzi twarz użytkownika.
7. Selfie Segmenter oddziela użytkownika od tła.
8. W zależności od aktywnego trybu nakładana jest maska lub rozmywane jest tło.

---

## Ograniczenia

* Program wymaga dobrej widoczności dłoni.
* Skuteczność rozpoznawania zależy od jakości kamery.
* Gesty wykonywane zbyt szybko mogą nie zostać poprawnie wykryte.
* Projekt został przygotowany do celów edukacyjnych.

---

## Informacje dodatkowe

Projekt wykorzystuje gotowe modele sztucznej inteligencji MediaPipe oraz techniki Computer Vision do rozpoznawania gestów i twarzy w czasie rzeczywistym.

Projekt został wykonany wyłącznie w celach edukacyjnych jako projekt zaliczeniowy z przedmiotu:

**Metody sztucznej inteligencji**
