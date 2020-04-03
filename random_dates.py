
# مقایسه ترتیب دو آبجکت تاریخ. برای استفاده در مرتب سازی

def earlier_than(ic, cc):

    if ic["year"] < cc["year"]:
      return True

    elif ic["year"] == cc["year"] and ic["month"] < cc["month"]:
      return True

    elif ic["year"] == cc["year"] and ic["month"] == cc["month"] and ic["day"] < cc["day"]:
      return True

    return False

# فانکشن مرتب سازی
def sort_dates(a):
  i = 0
  while i < len(a):
     if earlier_than( a[i+1], a[i] ):
            t = a[i]
            a[i] = a[i+1]
            a[i+1] = t
            i = -1
     i = i+1

# تولید یک تاریخ رندم
# نویسنده: ندا
def date():
  import random
  a={}
  y=random.randint(1000,1001)
  m=random.randint(1,12)
  d=random.randint(1,30)
  a.update({"year":y});
  a.update({"month":m});
  a.update({"day":d});
  return a

# تولید آرایه ای پر از تاریخ های رندم
# نویسنده: ندا
def si(a):
  i=0
  b=[]
  c={}
  while i<7:
    a=date()
    #print((i+1), a["year"], a["month"], a["day"])
    b.append(a)
    c.update(a)
    print((i+1),c)
    i=i+1
  return b

# مرتب سازی (ناقص)
# نویسنده»: ندا
def comp (b):
  p=0
  while p<len(b)-1:
    #if b.value("year") in b[p]<b.value("year") in b[p+1]:
    #  if b.value("month") in b[p]<b.value("month") in b[p+1]:
    #    if b.value("day") in b[p]<b.value("day") in b[p+1]:
    if  earlier_than(b[p+1], b[p]):
        t = b[p+1]
        b[p+1] = b[p]
        b[p] = t
        p=-1

        #if b[p] ==b[p+1]:
        #  b.remove(b[p])
        #p=0
    p=p+1
  return

def print_dates(arr):
  p=0
  while p<len(arr):
    x = arr[p]
    print(p, x["year"], x["month"], x["day"])
    p=p+1

# بخش اصلی (main) برنامه:
# بعدش اجرای همه فانکشن ها:

a = si( None )
#sort_dates(a)
comp(a)
print_dates(a)
