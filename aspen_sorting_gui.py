import tkinter as tk
import random


NUM_OF_BARS = 20
DELAY = 200
SHAPE_COLOR = "pink"
BOARDER_COLOR = "blue"


root = tk.Tk()
canvas = tk.Canvas(root, bg="light blue", width=600, height=150)
root.title("Bubble Sort App")


def bubble_sort(canvas, shape_id_list):
    """_summary_

    Args:
        lst (list): _description_

    """
    n = len(shape_id_list)

    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if shape_id_list[i-1] > shape_id_list[i]:
                shape_id_list[i-1], shape_id_list[i] = shape_id_list[i], shape_id_list[i-1]
                swap_pos(shape_id_list[i-1], shape_id_list[i])
                swapped = True
    print("shape id list:", shape_id_list)


def create_bars(canvas):
    """Create 10 bars in a tkinter canvas widget, and return a list containing their IDs.

    Args:
        canvas (tk.Canvas): The canvas on which the bars will be drawn.
    
    Returns:
        list: A list containing the IDs of the bars created on the canvas.
    """
    # The following constants define the appearance and positioning of the bars.
    BAR_WIDTH = 15    # The width of each bar
    BAR_GAP = 15      # The gap between each bar
    MIN_HEIGHT = 10   # The minimum height a bar can have
    MAX_HEIGHT = 125  # The maximum height a bar can have
    X_OFFSET = 15     # The x-coordinate for the bars' left edge
    Y_OFFSET = 10     # The y-coordinate for the bars' top edge

    bar_id_list = []
    for count in range(NUM_OF_BARS):
        # Create a random height
        random_height = random.randint(MIN_HEIGHT, MAX_HEIGHT)
        print(random_height)

        bar_id = canvas.create_rectangle(
                                        # x0
                                        (BAR_WIDTH + BAR_GAP) * count + X_OFFSET,
                                        # y0
                                        (MAX_HEIGHT - random_height) + Y_OFFSET,
                                        # x1
                                        (BAR_WIDTH + BAR_GAP) * count + X_OFFSET + BAR_WIDTH,
                                        # y1
                                        MAX_HEIGHT + Y_OFFSET,
                                        fill=SHAPE_COLOR,
                                        outline=BOARDER_COLOR
                                        )
        bar_id_list.append(bar_id)

        # Show bar height beneath each bar
        x_text = (BAR_WIDTH + BAR_GAP) * count + X_OFFSET + 10
        y_text = MAX_HEIGHT + Y_OFFSET + 10
        canvas.create_text(x_text, y_text, text=f"{random_height}")

    return bar_id_list

# TODO: a function for moving the rectangles each time they are swapped in the bubble sort function


def swap_pos(pos01, pos02):
    """need to get the x coords of the bars i was to swap

    Args:
        pos01 (_type_): _description_
        pos02 (_type_): _description_
    """
    canvas.move(pos01, x_10-x_00, 0)
    canvas.move(pos02, x_01-x_11, 0)

bar_list = create_bars(canvas)
print("bar list:", bar_list)
sort_button = tk.Button(
        root,
        text="Sort",
        command=lambda: bubble_sort(canvas, bar_list) # does this work?
        )

canvas.grid(column=0, row=0)
sort_button.grid(column=0, row=2)


root.mainloop()

