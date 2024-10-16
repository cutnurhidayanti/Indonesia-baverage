import os

# Folder yang berisi file label
folder_path = 'Indonesia-Beverage-9/test/labels'

# Loop untuk membaca setiap file .txt di dalam folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        # Membuat path lengkap file
        file_path = os.path.join(folder_path, filename)

        # Membaca isi file
        file = open(file_path, 'r')
        data = file.read()
        file.close()  # Menutup file setelah dibaca

        # Split data menjadi baris-baris
        lines = data.strip().split("\n")

        # Buat list untuk menampung baris yang telah diperbarui
        updated_lines = []

        # Memproses setiap baris
        for line in lines:
            parts = line.split()
            label = int(parts[0]) + 1  # Increment label
            updated_line = f"{label} " + " ".join(parts[1:])
            updated_lines.append(updated_line)

        # Menggabungkan baris yang telah diperbarui menjadi satu string
        result = "\n".join(updated_lines)

        # Membuka kembali file untuk menulis hasil
        file = open(file_path, 'w')
        file.write(result)
        file.close()  # Menutup file setelah menulis

        print(f"Updated {filename}")
