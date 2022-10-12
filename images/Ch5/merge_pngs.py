from PIL import Image


img_01 = Image.open("MD5_overview_x_no_legend_2.png")
img_02 = Image.open("MD5_overview_y_no_legend_2.png")
img_03 = Image.open("bunch_length.png")

img_01_size = img_01.size
img_02_size = img_02.size
img_03_size = img_02.size

print('img 1 size: ', img_01_size)
print('img 2 size: ', img_02_size)
print('img 3 size: ', img_03_size)


new_im = Image.new('RGB', (img_01_size[0], 3*img_01_size[1]), (250,250,250))

new_im.paste(img_01, (0,0))
new_im.paste(img_02, (0, img_01_size[1]))
new_im.paste(img_03, (0, 2*img_01_size[1]))

new_im.show()
