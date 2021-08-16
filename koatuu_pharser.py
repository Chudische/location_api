import xlrd
import csv


class Item(object):
    places_three = []   

    def __init__(self, level1, level2, level3, level4, category, name):
        self.id = level4 or level3 or level2 or level1
        # remove region center from region name
        if name.find('/') > 0:
            self.name = name[:name.find('/')]
        else:
            self.name = name
        # set category to place
        if category == 'Р':
            self.category = 'РГ'
        elif self.name.endswith('РАЙОН'):
            self.category = 'РН'
        else:
            self.category = category
        # set parent id
        if level4:
            self.parent_id = level3            
        elif level3:
            self.parent_id = level2                          
        elif level2:
            self.parent_id = level1
        else:
            self.parent_id = None
        # set is_location flag
        if self.category in ('М', 'Т', 'С', 'Щ', 'РГ'):
            self.is_location = True
        else:
            self.is_location = False
        # set rating
        if self.category in ('М', 'РГ'):
            self.rating = 100
        elif self.category == 'Т':
            self.rating = 50
        elif self.category in ('С', 'Щ'):
            self.rating = 25
        else:
            self.rating = 0

        Item.places_three.append(self)


workbook = xlrd.open_workbook("./KOATUU_riv_26112020.xls")
worksheet = workbook.sheet_by_index(0)
for rx in range(1, worksheet.nrows):
    row = worksheet.row(rx)    
    Item(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value)

with open('.places.csv', 'w') as csv_file:
    writer = csv.writer(csv_file )
    writer.writerow(['id', 'parent_id', 'category', 'name', 'coordinates', 'rating', 'is_location', 'is_active'])
    for item in Item.places_three:
        writer.writerow([item.id, item.parent_id, item.category, item.name, None, item.rating, item.is_location, None])
