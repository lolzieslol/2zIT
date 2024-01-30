
def detectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):

        if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2:
            return False

        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2:
            return True

        elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
            return True

        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
            return True

        else:
            return False

    