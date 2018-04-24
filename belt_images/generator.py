from PIL import Image, ImageFont, ImageDraw

belt_widht = 1200
belt_height = 50
marker_widht = 50
outline_thickness = 6

outline_color = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
orange = (255, 73, 0)
green = (0, 167, 0)
blue = (10, 10, 190)
brown = (110, 29, 3)

def regular(color, name):
    image = Image.new('RGB', (belt_widht, belt_height))
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), (belt_widht, belt_height)], fill = color)
    draw.line([(0, 0), (0, belt_height)], fill = outline_color, width = outline_thickness)
    draw.line([(0, 0), (belt_widht, 0)], fill = outline_color, width = outline_thickness)
    draw.line([(belt_widht, belt_height), (0, belt_height)], fill = outline_color, width = outline_thickness)
    draw.line([(belt_widht, belt_height), (belt_widht, 0)], fill = outline_color, width = outline_thickness)
    image.save(name)

def marker(primary, secondary, name):
    offset = int(belt_widht * 0.82)
    image = Image.new('RGB', (belt_widht, belt_height))
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), (belt_widht, belt_height)], fill = primary)
    draw.rectangle([(offset, 0), (offset + marker_widht, belt_height)], fill = secondary)
    draw.line([(0, 0), (0, belt_height)], fill = outline_color, width = outline_thickness)
    draw.line([(0, 0), (belt_widht, 0)], fill = outline_color, width = outline_thickness)
    draw.line([(offset - int(outline_thickness / 2), 0), (offset - int(outline_thickness / 2), belt_height)], fill = outline_color, width = outline_thickness)
    draw.line([(offset + marker_widht - int(outline_thickness / 2), 0), (offset + marker_widht - int(outline_thickness / 2), belt_height)], fill = outline_color, width = outline_thickness)
    draw.line([(belt_widht, belt_height), (0, belt_height)], fill = outline_color, width = outline_thickness)
    draw.line([(belt_widht, belt_height), (belt_widht, 0)], fill = outline_color, width = outline_thickness)
    image.save(name)

marker(white, yellow, "gul_markering.png")
regular(yellow, "gult_balte.png")
marker(yellow, orange, "orange_markering.png")
regular(orange, "oranget_balte.png")
marker(orange, green, "gron_markering.png")
regular(green, "gront_balte.png")
marker(green, blue, "bla_markering.png")
regular(blue, "blat_balte.png")
marker(blue, brown, "brun_markering.png")
regular(brown, "brunt_balte.png")
