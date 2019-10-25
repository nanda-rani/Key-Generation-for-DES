def applyPC1(pc1,keys64):
 keys56 = ""
 for index in pc1:
    #print("Index:",index)
    keys56 += keys64[index-1] 
 return keys56

def split_half(keys56):
 lkeys, rkeys = keys56[:28],keys56[28:]
 return lkeys, rkeys

def clshift(bits,numberofbits):
 shiftbits = bits[numberofbits:] + bits[:numberofbits]
 return shiftbits

def applyPC2(pc2,keys56):
 keys48= ""
 for index in pc2:
  keys48 += keys56[index-1]
 return keys48

def generate_keys(key64):
 round_keys = list() 
 pc1_out = applyPC1(PC1,key64) 
 L0,R0 = split_half(pc1_out)
 for r in range(16):
  newL = clshift(L0,roundshifts[r])
  newR = clshift(R0,roundshifts[r])
  roundkey = applyPC2(PC2,newL+newR)
  round_keys.append(roundkey)
  L0 = newL
  R0 = newR
 return round_keys



PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
'''
key64=""
for i in range(64):
    key64 += input("Enter key bits")

print(key64)
'''
keys64 = "0001001100110100010101110111100110011011101111001101111111110001"
keys56 = applyPC1(PC1,keys64)
print("Key56:\n",keys56)

left56 , right56 = split_half(keys56)

lhalf=clshift(left56,len(left56))
rhalf=clshift(right56,len(right56))


PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2, 41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
subkey = applyPC2(PC2,lhalf + rhalf)

roundshifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
subkeys = generate_keys(keys64)

print ("Subkeys:\n",subkeys)
