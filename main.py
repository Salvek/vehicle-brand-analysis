import os
from ultralytics import YOLO

def main():
    video_path = os.path.join("data", "raw", "test_wideo.mp4")
    
    if not os.path.exists(video_path):
        print(f"BŁĄD: Nie znaleziono pliku {video_path}!")
        return

    print("1. Ładowanie modelu...")
    model = YOLO("yolov8n.pt")

    print(f"2. Rozpoczynam analizę pliku: {video_path}")
    
    # ZMIANA: show=False (nie pokazuj okienka), save=True (zapisz wynikowy plik wideo)
    results = model.predict(source=video_path, show=False, save=True, stream=True)

    print("3. Przetwarzam klatki...")
    nr_klatki = 1
    for r in results:
        # Pokaż znak życia w konsoli co 30 przetworzoną klatkę
        if nr_klatki % 30 == 0:
            print(f"   Przetworzono klatkę nr: {nr_klatki}")
        nr_klatki += 1

    print("4. Analiza zakończona!")
    print("Sprawdź folder główny Twojego projektu. Powinien tam powstać folder 'runs/detect/predict/', a w nim gotowe wideo!")

if __name__ == "__main__":
    main()