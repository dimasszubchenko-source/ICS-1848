import math

print("Введіть координати точки M:")
mx = float(input("  x: "))
my = float(input("  y: "))

print("\nВведіть координати точки A:")
ax = float(input("  x: "))
ay = float(input("  y: "))

print("\nВведіть координати точки B:")
bx = float(input("  x: "))
by = float(input("  y: "))

print("\nВведіть координати точки C:")
cx = float(input("  x: "))
cy = float(input("  y: "))



dist_A = math.sqrt((ax - mx)**2 + (ay - my)**2)
dist_B = math.sqrt((bx - mx)**2 + (by - my)**2)
dist_C = math.sqrt((cx - mx)**2 + (cy - my)**2)

print(f"\nВідстань до точки A: {dist_A:.3f}")
print(f"Відстань до точки B: {dist_B:.3f}")
print(f"Відстань до точки C: {dist_C:.3f}")


if dist_A > dist_B and dist_A > dist_C:
    print("\nНазва точки, відстань від якої до точки M найбільша: A")
elif dist_B > dist_C and dist_B > dist_A:
    print("\nНазва точки, відстань від якої до точки M найбільша: B")
else:
    print("\nНазва точки, відстань від якої до точки M найбільша: C")
