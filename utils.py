import math


def scale(distance, coef=50):

    return 1.0 / math.exp(distance / coef)


def dist(x1, x2, y1, y2):

    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def is_collide(x1, x2, y1, y2, r1, r2):

    d = dist(x1, x2, y1, y2)
    return d <= (r1 + r2)


def angle(x1, x2, y1, y2):

    return (math.atan2(y1 - y2, x1 - x2) / math.pi * 180 + 180) % 360


def sector(angle, spectrum):

    angle = angle % 360
    return int(angle // math.ceil(360 / spectrum))


def main():
     pass


if __name__ == "__main__":
    main()
