from tkinter import*
import requests
root = Tk()
root.title("Weather App")
root.iconbitmap('weather.ico')
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
textInput = Label(topFrame, text='Type in the city below')
cityEntry = Entry(topFrame, text='Type in the city')
tempOut = Label(topFrame, text='The current temp is:')


def getWeatherTemp():
    content = cityEntry.get()
    api_address = 'http://api.openweathermap.org/data/2.5/forecast?q=' + content + '&units=imperial&&apikey=004efc69e1c7010c6f3300fe896b35d5'
    url = api_address
    json_data = requests.get(url).json()
    temp = str(json_data['list'][0]['main']['temp'])
    tempmin = str(json_data['list'][0]['main']['temp_min'])
    tempmax = str(json_data['list'][0]['main']['temp_max'])
    tempOut.config(text='The current temp is: ' + temp)
    root2 = Tk()
    tFrame = Frame(root2)
    tFrame.pack()
    tempOutt = Label(tFrame, text='The current temp is: ' + temp)
    tempOuttMin = Label(tFrame, text='The minimum temperature today is: ' + tempmin)
    tempOuttMax = Label(tFrame, text='The maximum temperature today is: ' + tempmax)
    tempOutt.pack(ipadx=5, ipady=5)
    tempOuttMin.pack(ipadx=5, ipady=5)
    tempOuttMax.pack(ipadx=5, ipady=5)
    root.mainloop()


button1 = Button(bottomFrame, text='Get Temperature', fg='white', bg='black', command=getWeatherTemp)
textInput.pack(ipadx=50, ipady=25)
cityEntry.pack()
button1.pack()
tempOut.pack(ipadx=10, ipady=10)
root.mainloop()
