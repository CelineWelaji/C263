from flask import flask, render_template, request
import requests

app = flask(__name__)

@app.route('/')
def visitors():

	visitors_count = visitors_count+1
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

	render_template("index.html",count=visitors_count)

@app.route("/",methods=["POST"])
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	latitude = request.form['latitude']
	longitude = request.form['longitude']

	api = "https://weather-l6tl.onrender.com/api/getCurrentWeather/"+latitude+"/"+longitude

	response = requests.get(api)
	weatherData = response.json()
	print(weatherData)
	return render_template("index.html",weather=weatherData,count=visitors_count)

#add code for executing flask