import math as m
length = 15
breadth = 5
lb = length + breadth

p = 2 * (lb)

a = length * breadth
d = m.sqrt((m.pow(breadth,2)) + (m.pow(length,2)))
print("The perimeter of the rectange is: %.4f" %p)
print("The area of the rectange is: %.4f" %a)
print("The diagonal of the rectange is: %.4f" %d)

radius = 10

circle_area = 2*(m.pi)*radius

circle_cir = (m.pi)*(m.pow(radius,2))
print("The area of the circle is: %.4f" %circle_area)
print("The circumference of the circle is: %.4f" %circle_cir)
