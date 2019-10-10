first_parts = ["Ask-i", "Avrupa", "Asmali", "Yaprak", "Tatli", "Arka", "Cocuklar"]
second_parts = ["Memnu", "Yakasi", "Konak", "Dokumu", "Hayat", "Sokaklar", "Duymasin"]

ind = 0
last_ind = len(first_parts)-1


while ind <= last_ind:
  full_name = first_parts[ind] + ' ' + second_parts[ind]
  print(full_name)
  ind += 1
