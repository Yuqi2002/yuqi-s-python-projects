# menus project(class)




brunch_items={'pancakes': 7.50, 'waffles': 9.00,
 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 
 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50,
  'orange juice': 3.50}

early_bird_items={'salumeria plate': 8.00,
 'salad and breadsticks (serves 2, no refills)': 14.00, 
 'pizza with quattro formaggi': 9.00,
  'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
   'coffee': 1.50, 'espresso': 3.00,}

dinner_items={'crostini with eggplant caponata': 13.00, 
'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 
 'coffee': 2.00, 'espresso': 3.00,}

kids_items={'chicken nuggets': 6.50, 
'fusilli with wild mushrooms': 12.00, 
'apple juice': 3.00}

menus=[brunch_items,early_bird_items,dinner_items,kids_items]

class Menu:
    def __init__(self,name,items,start_time,end_time):
        self.name=name
        self.items=items
        self.start_time=start_time
        self.end_time=end_time

    def __repr__(self):
        return self.name+' menu is available from ' + str(self.start_time)+ ' - ' + str(self.end_time)

    def calculate_bill(self,purchased_items):
        bill=0
        for x in purchased_items:
            if x in self.items:
                bill+=self.items[x]
        return bill 

brunch=Menu('Brunch',brunch_items,1100,1600)
print(brunch)

early_bird=Menu('Early Bird',early_bird_items,1500,1800)
print(early_bird)

Dinner=Menu('Dinner',dinner_items,1700,2300)
print(Dinner)

kids=Menu('Kids menu',kids_items,1100,2100)
print(kids)

print(brunch.calculate_bill(['pancakes','home fries','coffee']))

print(early_bird.calculate_bill(['mushroom ravioli (vegan)','salumeria plate']))



class Franchise:
    def __init__(self,address,menus):
        self.address=address
        self.menus=menus
    def __repr__(self):
        return self.address
    def available_menus(self,time):
        avaible_menus=[]
        for menu in self.menus:
            if time >=menu.start_time and time<= menu.endtime:
                avaible_menus.append(menu)
        return avaible_menus

Flagship=Franchise("1232 West End Road", menus)
new_installment=Franchise("12 East Mulberry Street",menus)
print(Flagship)

print(Flagship.available_menus(1200))