import numpy as np 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
from tensorflow.keras.models import load_model 
import tensorflow as tf

tf.compat.v1.enable_eager_execution()
print("Eager execution enabled:", tf.executing_eagerly())

iris = load_iris() 
X = iris.data 
y = iris.target 

scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 

encoder = OneHotEncoder(sparse_output==False) 
y_encoded = encoder.fit_transform(y.reshape(-1, 1)) 

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, 
random_state=42) 

X_train = np.array(X_train)
y_train = np.array(y_train)

model = load_model('iris_model.h5')
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10) 

model.save('updated_iris_model.h5') 

test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0) 
print(f"Test Accuracy: {test_accuracy*100:.2f}%")