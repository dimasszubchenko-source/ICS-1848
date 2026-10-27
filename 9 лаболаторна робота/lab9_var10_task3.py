months = ("January", "February", "March",
          "April", "May", "June",
          "July", "August", "September",
          "October", "November", "December")

A = {}
for month in months:
    A[month] = input(month + " українською: ")

B = {}
for key in A:
    B[A[key]] = key

print("Українсько-англійський словник:")
for key in B:
    print(key, "-", B[key])
