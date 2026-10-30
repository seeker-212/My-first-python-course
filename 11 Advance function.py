# ip = "192.168.56.128"
# def attack(ip):
#     print(ip)
# attack(ip)

print('Please enter the dimension of the room in sqft')

def calculate_area(w, h):
    area_sqft = w + h
    print(f"The total area is: {area_sqft}")
width = int(input("Enter the width of the room: "))
height = int(input("Enter the height of the room: "))

calculate_area(width, height)