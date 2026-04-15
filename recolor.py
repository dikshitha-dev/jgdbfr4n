from PIL import Image

img = Image.open('assets/logo.png').convert('RGBA')
data = img.getdata()

target_color = (245, 245, 220)
new_data = []

for r, g, b, a in data:
    # If pixel is opaque
    if a > 50:
        # If it's not white (r,g,b > 240 is white-ish)
        if r < 240 or g < 240 or b < 240:
            # It's the red logo part, change to beige with original alpha
            new_data.append((target_color[0], target_color[1], target_color[2], a))
        else:
            # Make white background transparent
            new_data.append((255, 255, 255, 0))
    else:
        new_data.append((r, g, b, a))

img.putdata(new_data)
img.save('assets/logo_beige.png', 'PNG')
print("Successfully recolored to beige")
