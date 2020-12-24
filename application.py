
#Import the necessary libraries
from flask import Flask, render_template, request

import pickle

application = Flask(__name__)               #initializing a flask app

@application.route('/',methods=['GET'])         #route to display the home page
def homePage():
    return  render_template("index.html")

@application.route('/predict',methods=['POST','GET'])           #route to display predictions
def index():
    if request.method == 'POST':
        try:
            #reading the inputs from the user
            age = int(request.form['age'])
            time = int(request.form['time'])
            serum_creatinine = float(request.form['serum_creatinine'])
            ejection_fraction = int(request.form['ejection_fraction'])

            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))        #Loading the saved model file
            #Predictions using the model
            prediction = loaded_model.predict([[age,time,serum_creatinine,ejection_fraction]])
            print('Prediction is', prediction)
            #Displaying the prediction results in a UI
            return render_template('results.html',prediction=prediction)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something went wrong'
        #else return render_template('results.html)
    else:
         return render_template(('index.html'))



if __name__ == "__main__":
    application.run(debug=True)