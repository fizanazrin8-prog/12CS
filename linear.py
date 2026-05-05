import stream as st
import panda as pd
from sklearn.model_selection import train_test_split
from sklear.linear_model import LinearRegression
df=pd.read_csv("student_scores.csv")
X=df.iloc[:, :-1].values
Y=df.iloc[:, -1].values
X_train,X_test,Y_train,Y_test=train_test_slpit(X,Y test_size=0.2, random=42)
model=LinearRgression()
model.fit(X_train,Y_train)
st.title("Exam score prediction model")
st.write("Enter the number of hours you studied for the exam")
hours=st.number_input("Hours studied",min_value=0.0, step=0.1)
if st.button"Predict score"):

