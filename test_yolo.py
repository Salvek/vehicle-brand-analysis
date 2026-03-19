print("Importuję bibliotekę (to może chwilę potrwać za pierwszym razem)...")
from ultralytics import YOLO

print("Inicjalizuję model...")
model = YOLO("yolov8n.pt") # Jeśli jeszcze nie pobrał modelu, zrobi to teraz

print("Analizuję zdjęcie testowe z internetu...")
# Analizujemy zdjęcie i zapisujemy wynik
results = model.predict(source="https://ultralytics.com/images/bus.jpg", save=True)

print("Koniec testu 2! Poszukaj folderu 'runs/detect/predict/' i zobacz czy jest tam zdjęcie z ramkami.")