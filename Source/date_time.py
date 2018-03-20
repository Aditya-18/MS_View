import datetime
import malespeaker


def current_date_time():
    dt = datetime.datetime.now()
    d = dt.hour

    f = 0
    if d > 12:
        d -= 12
        f = 1
    e = ""
    time = str(d) + ":" + str(dt.minute)
    if f == 1:
        time += " PM"
        e = " PM"
    else:
        time += " AM"
        e = " AM"

    print(time)
    malespeaker.speak(str(d) + " " + str(dt.minute) + " " + e)
    s = ""
    if dt.weekday == 1:
        s += "Sunday, "
    elif dt.weekday == 2:
        s += "Monday, "
    elif dt.weekday == 3:
        s += "Tuesday, "
    elif dt.weekday == 4:
        s += "Wednesday, "
    elif dt.weekday == 5:
        s += "Thursday, "
    elif dt.weekday == 6:
        s += "Friday, "
    elif dt.weekday == 7:
        s += "Saturday, "
    s += str(dt.day)
    d = dt.month
    if d == 1:
        s += " January "
    elif d == 2:
        s += " February "
    elif d == 3:
        s += " March "
    elif d == 4:
        s += " April "
    elif d == 5:
        s += " May "
    elif d == 6:
        s += " June "
    elif d == 7:
        s += " July "
    elif d == 8:
        s += " August "
    elif d == 9:
        s += " September "
    elif d == 10:
        s += " October "
    elif d == 11:
        s += " November "
    elif d == 12:
        s += " December "

    s += str(dt.year)
    print(s + " (IST)")
    malespeaker.speak(s)


if __name__ == '__main__':
    current_date_time()
