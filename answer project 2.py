# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded1

def isPointInCircle(x,y,r,center=(0,0)):
  if ((center[0]-x)**2) + ((center[1]-y)**2) <= r**2:
    return True
  else:
    return False
  pass
#CEK OUTPUT KODE ANDA
print(isPointInCircle(1,1,1,center=(0,0)),isPointInCircle(1,0,1,center=(0,0)),
      isPointInCircle(1,1,1,center=(1,0)),isPointInCircle(0,0,1,center=(1,1)))

#Graded2
import random
def generateRandomSquarePoints(n,length,center=(0,0)):
  minx = center[0]-length/2
  miny = center[1]-length/2
  maxx = minx+length
  maxy = miny+length
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  points = [[random.uniform(minx,maxx),random.uniform(miny, maxy)] for i in range(n)]
  return points
  pass
#CEK OUTPUT KODE ANDA
random.seed(0)

# generate 100 point di dalam persegi dengan panjang sisi 1 dan berpusat di (0,0)
points = generateRandomSquarePoints(100,1)
print(points[10:15])

#CEK OUTPUT KODE ANDA VISUALISASI
# Mari kita Visualisasikan 
# Jika sama dengan gambar di bawah ini maka keluaran sesuai harapan
import matplotlib.pyplot as plt
x,y = zip(*points)

# persegi dengan panjang sisi 1 dan berpusat di (0,0)
r1 = plt.Rectangle((-0.5,-0.5),1,1,color='r', fill=False)
c1 = plt.Circle((0,0), 0.5, color='b', fill=False)
fig, ax = plt.subplots(figsize=(9,9)) 
ax.add_artist(r1)
ax.add_artist(c1)
plt.xlim(-0.6,0.6)
plt.ylim(-0.6,0.6)
plt.scatter(x,y,s=100,marker='x')
plt.show()

#Graded3

def MCCircleArea(r,n=100,center=(0,0)):
  # MULAI KODEMU DI SINI
  titik = generateRandomSquarePoints(n,r*2,center)
  titik_dlink = [j for j in range(len(titik)) if isPointInCircle(titik[j][0],titik[j][1],r,center)]
  titik_dlink = len(titik_dlink)
  luas_link = titik_dlink/n * ((r*2)**2)
  return luas_link
  pass
#CEK OUTPUT KODE ANDA
random.seed(0)
print(MCCircleArea(1,100),MCCircleArea(1,10,center=(10,10)))

#Graded4

def LLNPiMC(nsim,nsample):
  # MULAI KODEMU DI SINI
  srch_pi = (MCCircleArea(1,nsample) for i in range(nsim))
  pi = sum(srch_pi)/nsim
  return pi
  #CEK OUTPUT KODE ANDA

import math

random.seed(0)
estpi = LLNPiMC(10000,500)

print('est_pi:',estpi)
print('act_pi:',math.pi)


# Graded5
def relativeError(act,est):
  # MULAI KODEMU DI SINI
  E = abs((est-act)/act)*100
  return E
  pass
#CEK OUTPUT KODE ANDA
print('error relatif:',relativeError(math.pi,estpi),'%')
