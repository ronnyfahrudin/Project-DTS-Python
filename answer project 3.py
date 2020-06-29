# nama file p3.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini
# Graded1
def caesar_encript(txt,shift):
    pass
    encrypted = ""
    for i in txt:
        if i.isupper(): 
            i_index = ord(i) - ord('A')
            i_shifted = (i_index + shift) % 26 + ord('A')
            i_new = chr(i_shifted)
            encrypted += i_new
        elif i.islower(): 
            i_index = ord(i) - ord('a') 
            i_shifted = (i_index + shift) % 26 + ord('a')
            i_new = chr(i_shifted)
            encrypted += i_new
        else:
            encrypted += i

    return encrypted
# Fungsi Decript caesar
def caesar_decript(chiper,shift):
    return caesar_encript(chiper,-shift)
# Sanity check!!!

msg = 'Haloz DTS mania, MANTAPSZZZ!'
cpr = caesar_encript(msg,4)
txt = caesar_decript(cpr,4)


#Graded2
# Fungsi mengacak urutan
def shuffle_order(txt,order):
    return ''.join([txt[i] for i in order])

def deshuffle_order(sftxt,order):
    pass
    l_out = [0] * len(sftxt)
    for i, j in enumerate(order):
        l_out[j] = sftxt[i]
    return ''.join(l_out)

#graded3

# Graded
 
import math
 
# convert txt ke dalam bentuk list teks yang lebih pendek
# dan terenkrispi dengan urutan acak setiap batchnya
def send_batch(txt,batch_order,shift=3):
    tv = len(txt)%len(batch_order)
    if tv != 0:
        subtxt = txt + '_'*(len(batch_order)-tv)
    else:
        subtxt = txt
    lst = []
    bagian = math.ceil(len(subtxt)/len(batch_order))
    for i in range(bagian):
        sublst = ''
        for k in range(len(batch_order)):
            sublst += subtxt[len(batch_order)*i + k]
        sublst = caesar_encript(sublst,shift)
        lst.append(shuffle_order(sublst, batch_order))
    return lst

def receive_batch(batch_cpr,batch_order,shift=3):
    batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
    return ''.join(batch_txt).strip('_')
