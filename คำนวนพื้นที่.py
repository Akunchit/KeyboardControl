Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sawatdee():
    """ฟงชั่นนี้ใชีสำหรับสวัสดี """
    print('สวัสดีจร้าาา')

    
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sawatdee']
help(sawatdee)
Help on function sawatdee in module __main__:

sawatdee()
    ฟงชั่นนี้ใชีสำหรับสวัสดี

help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def Sawatdee():
    """ฟังชั่นนี้ใช้สำหรับสวัสดี"""
    print('สวัสดี')

    
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

help(sawatdee)
Help on function sawatdee in module __main__:

sawatdee()
    ฟงชั่นนี้ใชีสำหรับสวัสดี

def hello(friend)
SyntaxError: expected ':'
def hello(friend):
    print('Hi, {}'.format(friend))

    
hello('Jhon')
Hi, Jhon
def land(width,long)
SyntaxError: expected ':'
def land(width,long):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินแปลงนี้กว้าง: {} เมตร  ยาว: {} เมตร'.format(width,long)
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
          
SyntaxError: '(' was never closed
def land(width,long):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินแปลงนี้กว้าง: {} เมตร  ยาว: {} เมตร'.format(width,long)
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
          
SyntaxError: '(' was never closed
def land(width,long):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินแปลงนี้กว้าง: {} เมตร  ยาว: {} เมตร'.format(width,long)
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
          
SyntaxError: '(' was never closed
def land(width,long):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินแปลงนี้กว้าง: {} เมตร  ยาว: {} เมตร'.format(width,long))
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))

    

land(5,15)
ที่ดินแปลงนี้กว้าง: 5 เมตร  ยาว: 15 เมตร
ที่ดินแปลงนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินแปลงนี้มีพื้นที่: 18.75 ตารางวา
print(res)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(res)
NameError: name 'res' is not defined
def land(width,long):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินแปลงนี้กว้าง: {} เมตร  ยาว: {} เมตร'.format(width,long))
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    return cal_wa

res = land(5,15)
ที่ดินแปลงนี้กว้าง: 5 เมตร  ยาว: 15 เมตร
ที่ดินแปลงนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินแปลงนี้มีพื้นที่: 18.75 ตารางวา
primt(res)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    primt(res)
NameError: name 'primt' is not defined. Did you mean: 'print'?
prit(res)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    prit(res)
NameError: name 'prit' is not defined. Did you mean: 'print'?
print(res)
18.75
def land(width,long,prics=999888):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินแปลงนี้กว้าง: {} เมตร  ยาว: {} เมตร'.format(width,long))
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    return cal_wa * price

res = land(5,15)
ที่ดินแปลงนี้กว้าง: 5 เมตร  ยาว: 15 เมตร
ที่ดินแปลงนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินแปลงนี้มีพื้นที่: 18.75 ตารางวา
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    res = land(5,15)
  File "<pyshell#40>", line 7, in land
    return cal_wa * price
NameError: name 'price' is not defined. Did you mean: 'prics'?
>>> print(res)
18.75
>>> def land(width,long,price=999888):
...     cal = width * long
...     cal_wa = cal / 4
...     print('ที่ดินแปลงนี้กว้าง: {} เมตร  ยาว: {} เมตร'.format(width,long))
...     print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
...     print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
...     return cal_wa * price
... 
>>> def land(width,long,price=999888):
...     cal = width * long
...     cal_wa = cal / 4
...     print('ที่ดินแปลงนี้กว้าง: {} เมตร  ยาว: {} เมตร'.format(width,long))
...     print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
...     print('ที่ดินแปลงนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
...     calprice = cal_wa * price
...     return 'ที่ดินแปลงนี้ราคา: {:,.2f} บาท'.format(calprice)
... 
>>> res = land(5,15)
ที่ดินแปลงนี้กว้าง: 5 เมตร  ยาว: 15 เมตร
ที่ดินแปลงนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินแปลงนี้มีพื้นที่: 18.75 ตารางวา
>>> print(res)
ที่ดินแปลงนี้ราคา: 18,747,900.00 บาท
>>> land(5,15)
ที่ดินแปลงนี้กว้าง: 5 เมตร  ยาว: 15 เมตร
ที่ดินแปลงนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินแปลงนี้มีพื้นที่: 18.75 ตารางวา
'ที่ดินแปลงนี้ราคา: 18,747,900.00 บาท'
>>> land(5,15,1000000)
ที่ดินแปลงนี้กว้าง: 5 เมตร  ยาว: 15 เมตร
ที่ดินแปลงนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินแปลงนี้มีพื้นที่: 18.75 ตารางวา
'ที่ดินแปลงนี้ราคา: 18,750,000.00 บาท'
