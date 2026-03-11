import csv

# with open('data.csv', 'w', newline='') as babitaji:
#     jetha = csv.writer(babitaji)
#     jetha.writerow(['Son', 'Daughter', 'Total'])
#     jetha.writerows([
#         ['Tapu1', 'Sonu1', 2],
#         ['Tapu2', 'Sonu2', 4]
#     ])

#*----------------------------------------------------------

#create a function to add data to csv file

def add_data(son,daughter,total):
    with open('data.csv', 'a', newline='') as babitaji:
        jetha = csv.writer(babitaji)
        jetha.writerow([son,daughter,total])

# add_data('Tapu3', 'Sonu3', 6)
add_data('Tapu4', 'Sonu4', 6)