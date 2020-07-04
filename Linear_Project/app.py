from flask import Flask, render_template, request, jsonify
import pickle
import sklearn


app =Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template(('index.html'))

@app.route('/predict', methods=['POST','GET'])
def index():
    if (request.method =='POST'):
        try:
            mileage = int(request.form['mileage'])
            age_yrs = int(request.form['age_yrs'])
            loaded_model = pickle.load(open('model.pickle', 'rb'))
            prediction =loaded_model.predict([[mileage,age_yrs]])
            print('prediction is', prediction)
            return render_template('results.html', prediction=round(prediction[0],2))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
