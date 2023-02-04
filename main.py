import turtle as t
import requests, json
from tkinter import PhotoImage

city_name = input("Enter a city name: ")
city_name.replace(" ", "+")

r = t.Turtle()
icon_t = t.Turtle()
# t.speed(0)
s = t.Screen()


def draw_icon_helper(image_file_name):
  subsampled_image = PhotoImage(file=image_file_name).subsample(4)
  s.addshape(image_file_name, t.Shape("image", subsampled_image))

def get_icon(main):
  if main == "Thunderstorm":
    image_file_name = 'thunderstorm.gif'
    t.fillcolor('royalblue')
  elif main == "Drizzle":
    image_file_name = 'drizzle.gif'
    t.fillcolor('lightskyblue')
  elif main == "Rain":
    image_file_name = 'rainy.gif'
    t.fillcolor('skyblue')
  elif main == "Snow":
    image_file_name = 'snow.gif'
    t.fillcolor('lightcyan')
  elif main == "Clear":
    image_file_name = 'sunny.gif'
    t.fillcolor('lemonchiffon')
  elif main == "Clouds":
    image_file_name = 'cloud.gif'
    t.fillcolor('gainsboro')
  image_file_name = 'atmosphere.gif'
  t.fillcolor('mistyrose')
  return image_file_name
  

def draw_icon(image_file_name):
  t.penup()
  t.goto(-240, 100)
  t.pendown()
  t.begin_fill()
  for i in range(2):
    t.fd(480)
    t.rt(90)
    t.fd(250)
    t.rt(90)
  t.end_fill()
  
  t.penup()
  t.goto(150, 30)
  t.pendown()

  draw_icon_helper(image_file_name)
  t.shape(image_file_name)

  
def call_api(city_name):
  api_key = '7905fccc7e98ec3204624ffa811414aa'
  base_url = 'https://api.openweathermap.org/data/2.5/weather?'
  complete_url = base_url + "q=" + city_name + "&appid=" + api_key
  data = requests.get(complete_url).json()
  return data


# return an array --> [temperature, temp_min, temp_max]
def get_temperature(data):
  k_temp = data['main']['temp']
  f_temp = 1.8 * (k_temp - 273) + 32
  new_f = round(f_temp, 2)
  temp_min = (data['main']['temp_min'] - 273) * 1.8 + 32
  temp_max = (data['main']['temp_max'] - 273) * 1.8 + 32
  return [new_f, round(temp_min, 2), round(temp_max, 2)]



def draw_widget():
  # t.fillcolor('lightblue')

  # t.goto(100, 100)
  data = call_api(city_name)
  main = data['weather'][0]['main']
  temps = get_temperature(data)
  description = data['weather'][0]['description']

  image_file_name = get_icon(main)
  draw_icon(image_file_name)
  

  r.penup()
  r.goto(-220, -20)
  r.pendown()
  r.write(str(temps[0]) + "°F", font=("Arial", 45, 'normal'))
  r.penup()
  r.goto(-220, 55)
  r.write(str(city_name).title(), font=("Arial", 20, 'normal'))
  r.penup()
  r.goto(-220, -120)
  r.pendown()
  r.write("L:" + str(temps[1]) + "°F" + "\t  H:" + str(temps[2]) + "°F",
          font=("Arial", 20, 'normal'))
  r.penup()
  r.goto(-220, -60)
  r.pendown()
  r.write((description), font=("Arial", 20, 'normal'))

  s.mainloop()


draw_widget()
# get_temperature()
