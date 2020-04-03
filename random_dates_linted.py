import random

# مقایسه ترتیب دو آبجکت تاریخ. برای استفاده در مرتب سازی

def earlier_than(prev, next_):
    """
      مقایسه ی دو آبجکت (دیکشنری) تاریخ
      نوصسنده: سهیل
    """
    if prev["year"] < next_["year"]:
        return True

    if prev["year"] == next_["year"] and prev["month"] < next_["month"]:
        return True

    if prev["year"] == next_["year"] \
              and prev["month"] == next_["month"] \
              and prev["day"] < next_["day"]:
        return True

    return False

"""
# فانکشن مرتب سازی (استفاده نشده)
def sort_dates_sosi(arr):
  i = 0
  while i < len(arr):
     if earlier_than( arr[i+1], arr[i] ):
            t = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = t
            i = -1
     i = i+1
"""


def new_random_date():
    """
      تولید یک تاریخ رندم
      نویسنده: ندا
    """
    obj = {}
    # random.randint(1900,2020)
    y = random.randint(1000, 1001)
    m = random.randint(1, 12)
    d = random.randint(1, 30)
    obj.update({"year":y})
    obj.update({"month":m})
    obj.update({"day":d})
    return obj

def create_list_of_dates():
    """
      تولید آرایه ای پر از تاریخ های رندم
      نویسنده: ندا
    """
    i = 0
    arr = []
    c = {}
    while i < 7:
        obj = new_random_date()
        #print((i+1), obj["year"], obj["month"], obj["day"])
        arr.append(obj)
        c.update(obj)
        #print((i+1),c)
        i = i+1
    return arr

def sort_list_of_dates(b):
    """
      مرتب سازی
      نویسنده: ندا
    """
    i = 0
    while i<len(b)-1:
        #if b.value("year") in b[i]<b.value("year") in b[i+1]:
        #  if b.value("month") in b[i]<b.value("month") in b[i+1]:
        #    if b.value("day") in b[i]<b.value("day") in b[i+1]:
        if  earlier_than(b[i+1], b[i]):
            t = b[i+1]
            b[i+1] = b[i]
            b[i] = t
            i = -1

            #if b[i] == b[i+1]:
            #  b.remove(b[i])
            #i = 0
        i = i+1
    return

def print_list_of_dates(arr):
    """
    آرایه ای که هر عنصرش یک آبجکت (دیکشنری = تاریخ)‌است را چاپ میکند.
    """
    i = 0
    while i<len(arr):
        x = arr[i]
        print(i, x["year"], x["month"], x["day"])
        i = i+1

"""
  بخش اصلی (main) برنامه:
  بعدش اجرای همه فانکشن ها:
"""

my_date_array = create_list_of_dates()
#sort_dates(my_date_array)
sort_list_of_dates(my_date_array)
print_list_of_dates(my_date_array)
