from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
hours_studied = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
exam_scores = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]
X = hours_studied
y = exam_scores
model = LinearRegression()
model.fit(X, y)
try:
  user_input = float(input("Enter hours studied: "))
  predicted_score = model.predict([[user_input]])[0]
  print(f"Predicted exam score: {predicted_score:.2f}")
except ValueError:
  print("Please enter a valid number.")
plt.scatter(
    [h[0] for h in hours_studied],
    exam_scores,
    color="blue",
    label="Actual Data",
)
plt.plot(
    [h[0] for h in hours_studied],
    model.predict(hours_studied),
    color="red",
    label="Regression Line",
)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Study Hours vs. Exam Score")
plt.legend()
plt.grid(True)
plt.show()