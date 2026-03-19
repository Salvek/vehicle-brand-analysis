import os
# TO JEST TA MAGICZNA LINIJKA - ignoruje konflikty DLL
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

print("1. Magiczna linijka wczytana. Próbuję zaimportować PyTorcha...")
import torch

print("2. Sukces! PyTorch załadowany. Próbuję YOLO...")
from ultralytics import YOLO

print("3. UDAŁO SIĘ! Jesteśmy w domu.")