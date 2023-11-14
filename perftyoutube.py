from pytube import YouTube
import re

def get_video_id(url):
    # Mencari ID video menggunakan regular expression
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

def download_video(url, output_path='.'):
    try:
        video_id = get_video_id(url)
        if video_id:
            # Mendapatkan objek YouTube berdasarkan ID video
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")

            # Memilih stream dengan kualitas tertinggi
            video_stream = yt.streams.get_highest_resolution()

            # Mendownload video ke output_path
            video_stream.download(output_path)

            print("Unduhan selesai!")
        else:
            print("ID video tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

# Meminta pengguna untuk memasukkan URL video
video_url = input("Masukkan URL video YouTube: ")
download_video(video_url, "../youtube")
