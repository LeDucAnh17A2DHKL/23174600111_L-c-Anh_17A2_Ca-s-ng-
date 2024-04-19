def so_sang_chu(so):
    chu_so = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    return ' '.join(chu_so[int(chu)] for chu in str(so))

so = int(input("Please enter a number: "))
print(f"The number {so} in English is: {so_sang_chu(so)}")

