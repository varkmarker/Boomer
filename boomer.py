import pyautogui as py
from time import sleep
from colr import Colr as colr


class Colors:
    def red(data):
        print(colr().hex("#ff0000", data, rgb_mode=True))

    def rose(data):
        print(colr().hex("#ff0066", data, rgb_mode=True))

    def green(data):
        print(colr().hex("#00ff8d", data, rgb_mode=True))

    def gnome_green(data):
        print(colr().hex("#2ed1b4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#a8c836", data, rgb_mode=True))

    def dark_orange(data):
        print(colr().hex("#cf301b", data, rgb_mode=True))

    def light_gnome(data):
        print(colr().hex("#00ffc4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#7ed666", data, rgb_mode=True))

    def violet(data):
        print(colr().hex("#cc33ff", data, rgb_mode=True))

    def light_green(data):
        print(colr().hex("#21ff00", data, rgb_mode=True))

    def orange(data):
        print(colr().hex("#ff8e35", data, rgb_mode=True))

    def yellow(data):
        print(colr().hex("#fff300", data, rgb_mode=True))

    def sky_blue(data):
        print(colr().hex("#00ccff", data, rgb_mode=True))

    def blue(data):
        print(colr().hex("#0000ff", data, rgb_mode=True))

    def cream(data):
        print(colr().hex("#ff9999", data, rgb_mode=True))

    def dark_rose(data):
        print(colr().hex("#cc0066", data, rgb_mode=True))

    def dark_red(data):
        print(colr().hex("#cc0000", data, rgb_mode=True))

    def dark_green(data):
        print(colr().hex("#009933", data, rgb_mode=True))

    def light_blue(data):
        print(colr().hex("#6666ff", data, rgb_mode=True))


print(
    colr().hex(
        "#ff0000",
        """\n
    .########...#######...#######..##.....##.########.########.
    .##.....##.##.....##.##.....##.###...###.##.......##.....##
    .##.....##.##.....##.##.....##.####.####.##.......##.....##
    .########..##.....##.##.....##.##.###.##.######...########.
    .##.....##.##.....##.##.....##.##.....##.##.......##...##..
    .##.....##.##.....##.##.....##.##.....##.##.......##....##.
    .########...#######...#######..##.....##.########.##.....##""",
        rgb_mode=True,
    ),
    colr().hex("#ff8e35", "v1.0", rgb_mode=True),
)
null = ""
dash = null.center(58, "-")
Colors.light_blue("\n     " + dash)
print(
    colr().hex("#6666ff", "     |", rgb_mode=True),
    colr().hex(
        "#ff0000",
        " Please move your mouse cursor to your typing field. ",
        rgb_mode=True,
    ),
    colr().hex("#6666ff", " |", rgb_mode=True),
)
print(
    colr().hex("#6666ff", "     |", rgb_mode=True),
    colr().hex(
        "#ff0000", "     It has a limited time.So do it fast you can.", rgb_mode=True
    ),
    colr().hex("#6666ff", "     |", rgb_mode=True),
)
print(
    colr().hex("#6666ff", "     |", rgb_mode=True),
    colr().hex("#ff0000", "              Press Ctrl+c to stop it.", rgb_mode=True),
    colr().hex("#6666ff", "                |", rgb_mode=True),
)
Colors.light_blue("     " + dash)


def boom():
    try:
        try:
            limits = int(
                input(
                    colr().hex("#0000ff", "\n     Enter you limits  : ", rgb_mode=True)
                )
            )
            message = input(
                colr().hex("#0000ff", "     Enter you message : ", rgb_mode=True)
            )

        except ValueError:
            Colors.red("\n                       Invalid limit")
            exit()
        sleep(5)
        # For loop to print the message as the user set limits
        for limit in range(limits):
            py.typewrite(message)
            py.press("Enter")
            # if you want to time delay uncomment the below sleep command
            # sleep(3)
        boom()
    except KeyboardInterrupt:
        Colors.red("\n\n                         KeyboardInterrupt")
        exit()


boom()
