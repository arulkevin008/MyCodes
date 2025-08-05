print("\t\t\tHash Table")
bucket=[
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
    ]

try:
    def hash_function(name):
        sum_of_chars = 0
        for char in name:
            sum_of_chars+=ord(char)
        return sum_of_chars%10

    print(hash_function("Bob"))

    def add_element(name):
        index = hash_function(name)
        bucket[index].append(name)

    def look_element(name):
        index = hash_function(name)
        return name in bucket[index]
        
    add_element("Bob")
    add_element("Kevin")
    add_element("Saul")
    add_element("Donald")
    add_element("John")
    add_element("Walter")
    add_element("Hank")
    add_element("Peter")
    add_element("Jones")
    add_element("Stuart")
    print(look_element("Bob"))
    print(bucket)

except Exception as e:
    print("Error",e)
