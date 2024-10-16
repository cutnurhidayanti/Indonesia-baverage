import torch

# Mengecek apakah ada GPU yang tersedia
if torch.cuda.is_available():
    gpu_count = torch.cuda.device_count()
    print(f"Jumlah GPU tersedia: {gpu_count}")
    
    # Menampilkan nama masing-masing GPU
    for i in range(gpu_count):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("GPU tidak tersedia")
