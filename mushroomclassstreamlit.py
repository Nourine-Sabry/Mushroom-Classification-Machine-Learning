import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

st.title("Mushroom Classification: Edible or Poisonous?")
st.info("Input phenotypic mushroom characteristics to classify it as edible or poisonous [Disclaimer: Not an actual guide!].")

features = {
    'cap-shape': ['bell=b', 'conical=c', 'convex=x', 'flat=f', 'knobbed=k', 'sunken=s'],
    'cap-surface': ['fibrous=f', 'grooves=g', 'scaly=y', 'smooth=s'],
    'cap-color': ['brown=n', 'buff=b', 'cinnamon=c', 'gray=g', 'green=r', 'pink=p', 'purple=u', 'red=e', 'white=w', 'yellow=y'],
    'bruises': ['bruises=t', 'no=u'],
    'odor': ['almond=a', 'anise=l', 'creosote=c', 'fishy=y', 'foul=f', 'musty=m', 'none=n', 'pungent=p', 'spicy=s'],
    'gill-attachment': ['attached=a', 'descending=d', 'free=f', 'notched=n'],
    'gill-spacing': ['close=c', 'crowded=w', 'distant=d'],
    'gill-size': ['broad=b', 'narrow=n'],
    'gill-color': ['black=k', 'brown=n', 'buff=b', 'chocolate=h', 'gray=g', 'green=r', 'orange=o', 'pink=p', 'purple=u', 'red=e', 'white=w', 'yellow=y'],
    'stalk-shape': ['enlarging=e', 'tapering=t'],
    'stalk-root': ['bulbous=b', 'club=c', 'cup=u', 'equal=e', 'rhizomorphs=z', 'rooted=r', 'missing=?'],
    'stalk-surface-above-ring': ['fibrous=f', 'scaly=y', 'silky=k', 'smooth=s'],
    'stalk-surface-below-ring': ['fibrous=f', 'scaly=y', 'silky=k', 'smooth=s'],
    'stalk-color-above-ring': ['brown=n', 'buff=b', 'cinnamon=c', 'gray=g', 'orange=o', 'pink=p', 'red=e', 'white=w', 'yellow=y'],
    'stalk-color-below-ring': ['brown=n', 'buff=b', 'cinnamon=c', 'gray=g', 'orange=o', 'pink=p', 'red=e', 'white=w', 'yellow=y'],
    'veil-type': ['partial=p', 'universal=u'],
    'veil-color': ['brown=n', 'orange=o', 'white=w', 'yellow=y'],
    'ring-number': ['none=n', 'one=o', 'two=t'],
    'ring-type': ['cobwebby=c', 'evanescent=e', 'flaring=f', 'large=l', 'none=n', 'pendant=p', 'sheathing=s', 'zone=z'],
    'spore-print-color': ['black=k', 'brown=n', 'buff=b', 'chocolate=h', 'green=r', 'orange=o', 'purple=u', 'white=w', 'yellow=y'],
    'population': ['abundant=a', 'clustered=c', 'numerous=n', 'scattered=s', 'several=v', 'solitary=y'],
    'habitat': ['grasses=g', 'leaves=l', 'meadows=m', 'paths=p', 'urban=u', 'waste=w', 'woods=d']
}

label_encoders = {}

def encode_feature(data, feature):
    le = LabelEncoder()
    le.fit(data)
    label_encoders[feature] = le
    return le.transform(data)

def user_input_features():
    input_data = {}
    for feature, options in features.items():
        choice = st.selectbox(f"{feature.replace('-', ' ').capitalize()}:", options)
        choice = choice.split('=')[1] 
        input_data[feature] = encode_feature([choice], feature)[0]  
    return pd.DataFrame(input_data, index=[0])

input_df = user_input_features()

knn=pickle.load(open(r"C:\Users\Nourine\Desktop\mushrooms.sav",'rb'))

label_encoders['class'] = LabelEncoder()
label_encoders['class'].fit(['e', 'p'])

Con = st.sidebar.button('confirm')
if Con:
    result = knn.predict(input_df)
    prediction = label_encoders['class'].inverse_transform(result)[0]
    if prediction == 'e':
        st.sidebar.write("Mushroom is likely **edible**.")
    else:
        st.sidebar.write("Mushroom is likely **poisonous**.")