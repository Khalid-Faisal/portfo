from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home_Page():
	return render_template('index.html')

@app.route('/<string:page_name>')
def Index_Page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		database.write('\n{0},{1},{2}'.format(data['email'],data['subject'],data['message']))
def write_to_csv(data):
	with open('database.csv',newline='', mode='a') as database2:
		csv_writer = csv.writer(database2, delimiter = ',', quotechar= '"', quoting= csv.QUOTE_MINIMAL)
		csv_writer.writerow([data['email'],data['subject'],data['message']])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		try:
			data = request.form.to_dict()
			print(data)
			write_to_csv(data)
			write_to_file(data)
			return redirect('thanks.html')
		except:
			return 'Data Saving Failed !!'
	else:
		return 'Something Went Wrong !! Please Try After Sometime'