# nama file p1.py 
# Isikan nama anda dan copy semua cell code yang dengan komentar #Graded
#Ronny Fahrudin
priority = 0
priority = 1011
#netacad email cth: 'abcd@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded1

def letter_catalog(items,letter='A'):
  pass
  hasil = []
  for i in items:
    if(i[0]==letter):
      hasil.append(i)
  return hasil
# Cek output kode anda
print(letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='C'))

#Graded2

def counter_item(items):
  pass
  dc = {}
  for i in items:
    if i not in dc:
      dc[i] = 1
    else:
      dc[i] += 1
  return dc
# Cek output kode anda
print(counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries']))


#Graded3
# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
# MULAI KODEMU DI SINI
fruit_price = dict(zip(fruits, prices))

def total_price(dcounter,fprice):
  pass
  return sum(dcounter[k]*fprice[k] for k in dcounter)
# Cek output kode anda
print(total_price(counter_item(chart),fruit_price))

#Graded4
def discounted_price(total,discount,minprice=100):
  pass
  if total >= minprice:
    disc = total - (total * discount/100)
    return disc
  else:
    return total
# Cek output kode anda
print(discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100))


#Graded5
def print_summary(items,fprice):
  items = sorted(items)
  hitungitem = counter_item(items)
  hargaitem = fruit_price
  for i, k in hitungitem.items():
    print(k, i, ':', k*hargaitem[i])
  print('total :',total_price(counter_item(items),fprice))
  print("discount price :",discounted_price(total_price(counter_item(items),fprice),10,minprice=100))

print_summary(chart,fruit_price)


