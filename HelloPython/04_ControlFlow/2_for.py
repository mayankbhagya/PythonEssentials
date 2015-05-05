x = [1, 2, 3, 4, 5]


k = 6


# found = False
# for i in x:
#     if i == k:
#         found = True
#         break
# if found == False: raise Exception("Not found")



for i in x:
    if i == k: break
else:
    raise Exception("Not found")



