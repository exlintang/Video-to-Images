import cv2
import os

def video_to_images(video_path, output_folder, image_prefix='image_', image_format='jpg'):
  
    try:
        # Membuat folder output jika belum ada
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Membuka video
        video = cv2.VideoCapture(video_path)
        success, image = video.read()
        frame_count = 0

        while success:
            # Simpan setiap frame
            cv2.imwrite(os.path.join(output_folder, f"{image_prefix}{frame_count}.{image_format}"), image)
            frame_count += 1
            success, image = video.read()

        video.release()

        print(f"Sukses: Gambar disimpan di {output_folder}")

    except Exception as e:
        print("Gagal:", e)

# Ganti sesuai jalur yang dimiliki
video_path = 'file/video.mp4'  # Ganti dengan jalur video Anda
output_folder = 'folder/penyimpanan'  # Ganti dengan folder tujuan Anda
video_to_images(video_path, output_folder)
