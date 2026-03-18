# ============== Bank balansini yangilovchi funksiya yozing =================
def balans_yangila(balans,pul):
        yangi_balans = balans+pul
        return yangi_balans
    
balans = int(input("Mavjud balansingizni kiriting: "))
while True:
    pul = int(input("Qo'shmoqchi bo'lgan pulni kiriting: "))
    balans = balans_yangila(balans, pul)
    print(balans)
    chiqish = input("To'xtatish uchun 'stop' yozing: ")
    if chiqish == 'stop':
        break
    