from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

#dyanamic Routes selection
@app.route('/<string:page_source>')
def works(page_source):
    return render_template(page_source+'.html')

def write_to_file(data):
	with open('database.text', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file=database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_data', methods=["GET", "POST"])
def submit_data():
	if request.method == "POST":
		data = request.form.to_dict()
		#write_to_file(data)
		write_to_csv(data)		
		return redirect("./thankyou")
	return "Try to submit again..!"




# @app.route('/works')
# def works():
#     return render_template('works.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/components')
# def components():
#     return render_template('components.html')
