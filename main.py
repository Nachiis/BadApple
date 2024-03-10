import cv2
import numpy as np

# 读取视频
cap = cv2.VideoCapture('badapple.mp4')

# 创建 VideoWriter 对象，用于保存处理后的视频
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output_video.avi', fourcc, 30.0, (8, 7), isColor=False)

# 打开输出的文本文件
txt_file = open('output_hex.txt', 'w')
while cap.isOpened():
    ret, frame = cap.read()
    # if not ret:
    #     break

    # 将帧转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 压缩至 8x8 分辨率
    small_frame = cv2.resize(gray_frame, (8, 7))
    # print(small_frame)
    # print('')
    
    
    # # 处理每一列，计算二进制数
    # binary_str = ''
    
    

    
    
    for col in range(8):
        col_values = small_frame[:, col]
        binary_col = ''.join(['1' if val > 128 else '0' for val in col_values[::]])
        # binary_str += binary_col
        # print(binary_col)
    
        # 将二进制数转换为ascii
        hex_value = str(int(binary_col, 2))
        # print(hex_value)
        # 写入到文本文件
        txt_file.write(hex_value+"\n")

    # # 写入视频帧
    # out.write(small_frame)
    
    # #展示
    # cv2.imshow('frame',frame)
    # cv2.waitKey(0)
    # cv2.destroyWindow('frame')

txt_file.close()
cap.release()
out.release()
cv2.destroyAllWindows()
