#https://crm.o3team.ru/sellers/957988/tickets/366968615
#принимаем кучу текста и оставляем только номера отправлений (или артикулы товаров)
l = []
with (open(r'F:\asd.txt', encoding = 'utf-8') as file):
    content = file.read()
    for i in content:
        if i.isdigit() or i == '-':
            continue
        else:
            content = content.replace(i, ' ')
    c = 0
    content = content.split()
    for ar in content:
        if len(ar) > 7 and ar not in l:#  and ar[1] in '345':
            l.append(ar)


    print(len(l))
    print(*l, sep='\n')