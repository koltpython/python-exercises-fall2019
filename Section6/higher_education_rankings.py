# University Lists
koc_university = ["Koc University", (2018, 99), (2019, 100)]
sabanci_university = ["Sabanci University", (2018, 97), (2019, 98)]
bogazici_university = ["Bogazici University", (2018, 95), (2019, 94)]
metu_university = ["Metu University", (2018, 90), (2019, 93)]
bilkent_university = ["Bilkeny University", (2018, 96), (2019, 90)]

# List of All University Lists
universities = [koc_university, sabanci_university, bogazici_university, metu_university, bilkent_university]

# Your code starts here
def find_highest_rank(uni):
  max_pair = uni[1]
  for pair in uni[2:]:
    if pair[1] > max_pair[1]:
      max_pair = pair
  return max_pair
d = {}
for u in universities:
  d[u[0]] = find_highest_rank(u)
print(d)
  
  