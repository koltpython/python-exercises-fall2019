# a country name to statistics dictionary
data = {}
# a tuple that will contain column names of statistics
columns = None

# try to understand what this code does
with open('data.csv', 'r') as data_file:
  lines = data_file.readlines()
  # why did we use strip and split
  columns = tuple(lines[0].strip().split(',')[1:])
  for row in lines[1:]:
      row_data = row.strip().split(',')
      data[row_data[0]] = tuple(row_data[1:])
  data_file.close()
        
# create a new file called corruption.csv that contains only
# country names and corruption statistics
corruption_index = columns.index('Corruption')
with open('corruption.csv', 'w') as corruption_file:
  for country in data:
    corruption_str = country + ', ' + data[country][corruption_index] + '\n'
    corruption_file.write(corruption_str)
  corruption_file.close()
print('done')