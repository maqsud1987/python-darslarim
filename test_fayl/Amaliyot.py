# 1 - qism
with open('pi_million_digits.txt' ) as file:
    pi = file.read()
    
#print(pi)

#print(len(pi))

sana  = input("Tug'ilgan kininggizni kiriting(masalan 21021999)>>>")
if sana in pi:
    print("Topildi")
else:
    print("Topilmadi")
    
# 2 - qism

import pickle
with open('pi_data.pkl','wb') as f:
    pickle.dump(pi, f)

    
