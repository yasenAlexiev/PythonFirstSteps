from PIL import Image

word_matrix_image = Image.open("res\word_matrix.png")
print(word_matrix_image.size)

mask_image = Image.open("res\mask.png")
print(type(mask_image.size))

mask_image = mask_image.resize(word_matrix_image.size)
mask_image.putalpha(128)
print(mask_image.size)

word_matrix_image.paste(mask_image, box=(0,0), mask=mask_image)
word_matrix_image.show()
