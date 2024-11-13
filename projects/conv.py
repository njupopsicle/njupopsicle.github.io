from pdf2image import convert_from_path

# 设置 PDF 文件路径
pdf_path = 'method_en.pdf'

# 设置图像分辨率（DPI越高，图像越清晰）
dpi = 300

# 将PDF文件的每一页转换为高分辨率的PNG图像
images = convert_from_path(pdf_path, dpi=dpi)

# 保存每一页为单独的PNG图像
for i, image in enumerate(images):
    image.save(f'method_en_page_{i+1}.png', 'PNG')
