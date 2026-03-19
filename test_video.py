import cv2
import os

sciezka = os.path.join("data", "raw", "test_wideo.mp4")
print(f"Sprawdzam plik: {sciezka}")

cap = cv2.VideoCapture(sciezka)

if not cap.isOpened():
    print("BŁĄD: OpenCV nie potrafi otworzyć tego pliku! (Może zły format/kodek?)")
else:
    sukces, klatka = cap.read()
    if sukces:
        print(f"SUKCES! Przeczytałem pierwszą klatkę. Rozmiar: {klatka.shape}")
    else:
        print("BŁĄD: Plik istnieje, ale nie mogę przeczytać z niego obrazu.")

cap.release()
print("Koniec testu 1.")