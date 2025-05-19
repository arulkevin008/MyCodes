class laptop():
    price=""
    processor=""
    ram=""

hp = laptop()
dell = laptop()
lenovo = laptop()

hp.price="$899"
hp.processor="Intel i9-13900k"
hp.ram="32 gb ram"

dell.price="$799"
dell.processor="AMD Ryzen 5950x"
dell.ram="32 gb ram"

lenovo.price="$599"
lenovo.processor="AMD Ryzen 5950x"
lenovo.ram="16 gb ram"

print("HP")
print("Price:",hp.price)
print("Processor:",hp.processor)
print("Ram:",hp.ram)
print("\nDell")
print("Price:",dell.price)
print("Processor:",dell.processor)
print("Ram:",dell.ram)
print("\nLenovo")
print("Price:",lenovo.price)
print("Processor:",lenovo.processor)
print("Ram:",lenovo.ram)
