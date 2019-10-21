first_printing = [1, 1, 2, 11, 5, 8, 13, 2, 4]
second_printing = [2, 4, 5, 1, 6 , 8, 9, 3, 10, 13]

cerens_sheets = [ ]
recycle_bin = [ ]

# Your code starts here
for page in first_printing:
  if page in cerens_sheets:
    recycle_bin.append(page)
  else:
    cerens_sheets.append(page)
for page in second_printing:
  if page in cerens_sheets:
    recycle_bin.append(page)
  else:
    cerens_sheets.append(page)


cerens_sheets.sort()
print(f'Cerens sheets: {cerens_sheets}')
print(f'Recycled: {recycle_bin}')
