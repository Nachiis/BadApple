import keyboard
txt_file = open('output_hex.txt', 'r')
for line in txt_file:
    print(line.rstrip())
    keyboard.wait('a')