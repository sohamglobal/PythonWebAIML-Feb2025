import pandas
from sklearn.tree import DecisionTreeClassifier
import joblib

url="https://raw.githubusercontent.com/sohamglobal/datasets/refs/heads/main/fitnessdata.csv"
df=pandas.read_csv(url)
#print(df)

features=df[['Age','Weight','ExerciseTime']]
#print(features)
labels=df['FitnessLevel']
#print(labels)

model=DecisionTreeClassifier()
model.fit(features,labels)

joblib.dump(model,'fitness.joblib')
print('Trained model saved for future use')
