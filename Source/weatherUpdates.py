from weather import Weather
import malespeaker
import transcribe
import gui


def getWeather(q):
    weather = Weather()
    malespeaker.speak("Please tell me the city you are interested in")
    x = "I could not get that"
    while x == "I could not get that":
        x=transcribe.transcribe_file()

    print("city: "+x)
    # x=input()
    location = weather.lookup_by_location(x)
    condition = location.condition()
    #print(condition.text())

    # Get weather forecasts for the upcoming days.
    s=""
    forecasts = location.forecast()
    i=2



    for forecast in forecasts:
        s += forecast.text()
        s += "\n" + forecast.date()
        s += "\n Max" + forecast.high() + "(Degree Celsius) Min" + forecast.low() + "(Degree Celsius)"
        s += "\n\n"
        i += 1
        if i > 5:
            break
    print(s)
    malespeaker.speak(s)

if __name__ == "__main__":
    getWeather("hello")

