from PIL import Image

# 打开两个PNG图像
image1 = Image.open('1200px-NJU.svg.png')
image2 = Image.open('ustc_blue.png')

# 获取两个图像的尺寸
width1, height1 = image1.size
width2, height2 = image2.size

# 计算合并后图像的宽度和高度
new_width = max(width1, width2)
new_height = height1 + height2

# 创建一个新的图像，尺寸为合并后的宽度和高度
new_image = Image.new('RGBA', (new_width, new_height))

# 计算两个图像在合并后的位置
x_offset1 = (new_width - width1) // 2
x_offset2 = (new_width - width2) // 2

# 将第一个图像粘贴到新图像的顶部中心
new_image.paste(image1, (x_offset1, 0))

# 将第二个图像粘贴到新图像的底部中心
new_image.paste(image2, (x_offset2, height1))

# 保存合并后的图像
new_image.save('merged_image.png')