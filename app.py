

from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load medicine-dataframe from pickle
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)

# Load similarity-vector-data from pickle
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(medicine):
    #medicine = "Waklert 150mg Tablet 5"
    #print(medicine)
    matching_medicines = medicines[medicines['Drug_Name'].str.contains(medicine, case=False)]
    if matching_medicines.empty:
        return []  # No matching medicines found

    medicine_index = matching_medicines.index[0]
    #medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

li = list(medicines['Drug_Name'])
rm = []  # Assign an initial empty list to rm

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        rm = recommend(name)
    else:
        name = None
        rm = []  # Assign an empty list to rm when the request method is GET
    return render_template('index.html', name=name, medis=li, recmed=rm)

if __name__ == '__main__':
    app.run()
