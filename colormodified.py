import colorsys
from PIL import Image

# 输入文件
filename = 'output.png'
# 目标色值
target_vision = 0.61
target_sat = 0.7
# 读入图片，转化为 RGB 色值
image = Image.open(filename).convert('RGBA')

# 将 RGB 色值分离
image.load()
r, g, b, a = image.split()
result_r, result_g, result_b, result_a = [], [], [], []
# 依次对每个像素点进行处理
for pixel_r, pixel_g, pixel_b, pixel_a in zip(r.getdata(), g.getdata(), b.getdata(), a.getdata()):
    # 转为 HSV 色值
    h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_g / 255.)
    # 转回 RGB 色系
    rgb = colorsys.hsv_to_rgb(h, target_sat, target_vision)
    pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]
    # 每个像素点结果保存
    result_r.append(pixel_r)
    result_g.append(pixel_g)
    result_b.append(pixel_b)
    result_a.append(pixel_a)

r.putdata(result_r)
g.putdata(result_g)
b.putdata(result_b)
a.putdata(result_a)

# 合并图片
image = Image.merge('RGBA', (r, g, b, a))
# 输出图片
image.save('modified.png')