import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# 1. Load dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Normalize images
x_train = x_train / 255.0
x_test = x_test / 255.0

# 3. Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 classes (0-9)
])

# 4. Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train the model
model.fit(x_train, y_train, epochs=5, validation_split=0.1)

# 6. Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

# 7. Predict and visualize
predictions = model.predict(x_test)

# Plot some predictions
for i in range(5):
    plt.imshow(x_test[i], cmap='gray')
    plt.title(f"Prediction: {tf.argmax(predictions[i]).numpy()}")
    plt.axis('off')
    plt.show()
