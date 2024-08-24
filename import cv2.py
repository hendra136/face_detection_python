import cv2
import numpy as np

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Konversi ke grayscale (opsional, tergantung metode deteksi)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi objek (ganti dengan metode deteksi yang Anda pilih)
    # Contoh: Menggunakan Haar Cascades untuk deteksi wajah
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Gambar kotak di sekitar objek yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Tampilkan hasil
    cv2.imshow('Deteksi Objek', frame)

    # Keluar jika menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()