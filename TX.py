import serial
import time
import keyboard

#代码行执行打开串口及发送内容时，打开串口与发送内容之间要间隔0.5秒以上，不然无法发出内容
ser = serial.Serial('COM3', 9600)

txt_file = open('output_hex.txt', 'r')
line_count = 0

if ser.isOpen():
    print("串口打开")
    for line in txt_file:
        
        line_count += 1
        txt = chr(int(line.rstrip()))
        ser.write(txt.encode())#发送信息编解码可以utf-8，也可以使用ascii编码
        # print(bin(int(line)))
        # 检测是否有按键按下
        
        
        if line_count % 8 == 0:
            #break
            time.sleep(0.01666666)
            # keyboard.wait('a')
            # print()
ser.close()