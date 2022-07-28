"""
    Title: Colorwheel Demonstration
    Description: This demonstrates the ability of creating a color wheel color select in Tkinter
    Author: Israel Dryer
    Modified: 2020-05-30

"""
import tkinter as tk

root = tk.Tk()
root.title("Colorwheel")


def on_mouse_drag(event):
    """Mouse movement callback"""
    # get mouse coordinates
    x = event.x
    y = event.y

    # clear the canvas and redraw
    canvas.delete("all")
    canvas.create_image(365, 365, image=wheel)
    canvas.create_image(x, y, image=target)

    # get rgb color from pixel location in image
    rgb_color = wheel.get(x, y)

    # format the rgb color in hexadecimal
    hex_color = "#{:02x}{:02x}{:02x}".format(*rgb_color)

    # adjust the label background color and text
    color_label.set(hex_color + "\nrgb({},{},{})".format(*rgb_color))
    color_select["bg"] = hex_color


canvas = tk.Canvas(root, height=730, width=730)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
canvas.bind("<B1-Motion>", on_mouse_drag)

color_label = tk.StringVar()
color_label.set("#FFFFFF\nrgb(255,255,255)")
color_select = tk.Label(root, textvariable=color_label, bg="white", width=20, font=("Arial", 20, "bold"))
color_select.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

wheel = tk.PhotoImage(file="color_wheel.png")
target = tk.PhotoImage(file="target.png")

canvas.create_image(365, 365, image=wheel)
canvas.create_image(365, 365, image=target)

root.mainloop()
