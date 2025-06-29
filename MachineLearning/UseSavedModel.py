import joblib
import pandas

model=joblib.load('fitness.joblib')

newdata=pandas.DataFrame({'Age':[41],'Weight':[62],'ExerciseTime':[35]})
prediction=model.predict(newdata)
print('Fitness level prediction :',prediction)