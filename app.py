from flask import Flask,request,render_template
import pickle

app=Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_data",methods=["POST"])
def model_prediction():
    data=request.form
    print(data)
    model=pickle.load(open(r"C:\Users\Admin\Desktop\Project Dipo\diabeties\model.pkl","rb"))
    print(model)    

    user_data = [[float(data['Pregnancies']),
                  float(data['Glucose']),
                  float(data['BloodPressure']),
                  float(data['SkinThickness']),
                  float(data['Insulin']),
                  float(data['BMI']),
                  float(data['DiabetesPedigreeFunction']),
                  float(data['Age'])
                  ]]
    print(user_data)

    result = model.predict(user_data)

    print(result)
    target=['Positive','Negative']
    print(f"prediction = {target[result[0]]}")
    return target[result[0]]

if __name__=="__main__":
    app.run(debug=False,port=8080,host='0.0.0.0')
