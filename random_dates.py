def earlier_than(ic, cc):

    if ic["year"] < cc["year"]:
      return True

    elif ic["year"] == cc["year"] and ic["month"] < cc["month"]:
      return True

    elif ic["year"] == cc["year"] and ic["month"] == cc["month"] and ic["day"] < cc["day"]:
      return True

  return False


def sort_dates(a):
  i = 0
  while i < n:
     if earlier_than( a[i+1], a[i] ):
            t = a[i]
            a[i] = a[i+1]
            a[i+1] = t
            i = -1
     i = i+1
