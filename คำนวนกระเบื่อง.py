tilecolor = {'red':100,'gold':200,'white':90,'grey':30}
print('-----------โปรแกรมคำนวณกระเบื้อง by Kunchit---------')

print('---------ราคากระเบื้อง--------')
for c,t in tilecolor.items():
    print(งสี:{}ราคา:{}'.format(c,t)')
try: 
    tiles = int(input ('คุณต้องการปูกระเบื้องกี่แผ่น: '))
    row = int(input ('1 แถวต้องการปูกระเบื้อกี่แผ่น: ')) # 3 ชิ้นต่อแถว
    color=input('กระเบื้องสีอะไร? [red / gold / white ] : ')
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น')
    tiles = int(input ('คุณต้องการปูกระเบื้องกี่แผ่น: '))
    row = int(input ('1 แถวต้องการปูกระเบื้อกี่แผ่น: '))
    color=input('กระเบื้องสีอะไร? [red / gold / white ] : ')
    
print('-----------Calculate---------')
total_row = tiles // row
remain_tiles = tiles % row
#print(total_row,remain_tiles)

buy_more = row - remain_tiles
print(f'มีกระเบื้อทั้งหมด: {tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ {row} แผ่น')
print('--------คำนวณ-------')
print('ต้องปูกระเบื้องทั้งหมด  {} แถว' .format(total_row))
print('เหลื่อกระเบื้องยังไม่ได้ปูเต็มแถว {} แผ่น'.format(remain_tiles))
print('ลค ต้องชื้อกระเบื้องเพิ่ม {} แผ่น'.format(buy_more))
print('ยอดรวมทั้งหมดที่ต้องการซื้อกรเบื้องเพิ่ม: {} บาท'.format(buy_more * tilecolor[color]))

      

#ลค ต้องขื้อกระเบื้องเพิ่มกี่แผ่น
