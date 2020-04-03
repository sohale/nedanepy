
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
def new_random_date():
  import random
  a={}
  # random.randint(1900,2020)
  y=random.randint(1000,1001)
  m=random.randint(1,12)
  d=random.randint(1,30)
  a.update({"year":y});
  a.update({"month":m});
  a.update({"day":d});
  return a

# تولید آرایه ای پر از تاریخ های رندم
# نویسنده: ندا
def create_list_of_dates(a):
  i=0
  b=[]
  c={}
  while i<7:
    a=new_random_date()
    #print((i+1), a["year"], a["month"], a["day"])
    b.append(a)
    c.update(a)
    #print((i+1),c)
    i=i+1
  return b

# مرتب سازی (ناقص)
# نویسنده»: ندا
def sort_list_of_dates (b):
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

def print_list_of_dates(arr):
  i=0
  while i<len(arr):
    x = arr[i]
    print(i, x["year"], x["month"], x["day"])
    i=i+1

# بخش اصلی (main) برنامه:
# بعدش اجرای همه فانکشن ها:

a = create_list_of_dates( None )
#sort_dates(a)
sort_list_of_dates(a)
print_list_of_dates(a)
