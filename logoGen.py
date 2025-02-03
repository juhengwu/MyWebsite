from PIL import Image, ImageDraw, ImageFont

# 创建画布 (500x200 像素，透明背景)
img = Image.new('RGBA', (500, 200), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# 选择字体和大小 (如果本地有 Arial 粗体，可以改成 "arialbd.ttf")
font = ImageFont.truetype("arialbd.ttf", 80)

# 计算文本尺寸
bbox = font.getbbox("Juheng Wu")
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# 计算居中位置
x = (500 - text_width) / 2
y = (200 - text_height) / 2

# 创建文本图层
text_img = Image.new('RGBA', (500, 200), (255, 255, 255, 0))
text_draw = ImageDraw.Draw(text_img)
stroke_width = 3  # 描边宽度
stroke_color = "white"

# 先画白色描边
for dx in [-stroke_width, 0, stroke_width]:
    for dy in [-stroke_width, 0, stroke_width]:
        if dx != 0 or dy != 0:  # 避免覆盖原始文本
            text_draw.text((x + dx, y + dy), "Juheng Wu", font=font, fill=stroke_color)

# 画原始文本
text_draw.text((x, y), "Juheng Wu", font=font, fill="white")

# 计算 Shear 变换矩阵（向右倾斜 15 度）
shear_factor = 0.267  # tan(15°) ≈ 0.267
matrix = (1, shear_factor, 0, 0, 1, 0)

# 进行仿射变换，使文本倾斜
text_img = text_img.transform((500, 200), Image.AFFINE, matrix, resample=Image.BICUBIC)

# 叠加倾斜文本到原始画布
img.paste(text_img, (0, 0), text_img)
# 保存 PNG
img.save("juheng.png")

print("图片已保存为 juheng.png")