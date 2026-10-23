# Theory Questions#	
**1.	What is supervised machine learning?**
Supervised machine learning is a type of machine learning where the model is trained on a labeled dataset. This means every training example comes with both the input features (independent variables) and the correct target output or answer (dependent variable). The model learns patterns linking the inputs to the outputs so it can accurately predict outputs for new, unseen data.
**2.	What is unsupervised machine learning?**
Unsupervised machine learning is a type of machine learning where the model is trained on an unlabeled dataset. The algorithm is given raw input data without explicit target answers, outputs, or human instructions. The model analyzes the data independently to discover hidden patterns, underlying structures, groupings, or correlations on its own.
**3.	Explain the difference between supervised and unsupervised learning**
| Feature | Supervised Learning | Unsupervised Learning |
| :--- | :--- | :--- |
| **Data Input** | Labeled data (Input-Output pairs) | Unlabeled data (Input only) |
| **Goal** | Predict outcomes for new data | Discover hidden patterns and structures |
| **Complexity** | Simpler computationally | More computationally intensive |
| **Human Effort** | High (Requires manual data labeling) | Low (Data requires no labeling) |
| **Accuracy** | Highly accurate and verifiable | Less accurate, results need interpretation |
**4.	Why is Linear Regression considered supervised learning?**
Linear Regression is considered supervised learning because it requires explicit historical pairs of target variables (\(y\)) and predictor variables (\(X\)) during training. The algorithm directly maps mathematical changes in the inputs to minimize error margins against a known continuous answer sheet.
**5.	Why is K-Means considered unsupervised learning?**
K-Means is considered unsupervised learning because it operates entirely without predefined classes, categories, or labels. It accepts raw numerical matrices and dynamically groups rows based on geometric proximity (e.g., Euclidean distance metrics). It does not know what the resulting segments "mean" conceptually—it only identifies mathematical patterns in feature density.
**6.	 What is the difference between fit() and predict()?**
‘fit()’: The method that triggers the model's actual mathematical training logic. In supervised algorithms, it calculates coefficients, weights, or boundaries by analyzing inputs against outputs. In unsupervised algorithms (like scaling or clustering), it learns baseline metrics such as column means, variances, or initial cluster centers. 
‘predict()’: The execution method used *after* a model has been fit. It applies the learned parameters to new or existing input data points to assign them to a cluster category or calculate a numeric prediction vector.
**7.	Give two real-world applications of supervised learning and two of unsupervised learning.**
Supervised Learning Applications:  
Email Spam Filters: Classifying incoming mail collections into "Spam" or "Not Spam" categories based on labeled text histories. 
 Loan Default Risk Prediction: Predicting whether a credit applicant will default on a loan based on past labeled payment histories. 
Unsupervised Learning Applications:
Market Basket Analysis: Identifying which retail grocery items are frequently purchased together to optimize product placements on shelves. 
Anomaly Detection: Sifting through millions of banking transactions to flag unusual, outlying spending patterns that could signify credit card fraud.


