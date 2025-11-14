🛍️ E-commerce Sales Analysis & Predictive Modeling (2024 Dataset)

Author: Swathi Mulkundkar
Course: Data Analytics with AI – Code Institute
Submission Date: 14 November 2025

📘 Project Summary

This project analyzes the 2024 E-commerce Sales dataset using a complete Python-based ETL pipeline built with Pandas, NumPy, and Jupyter Notebook. The merged dataset enabled insights into category conversion rates, payment method behavior, and monthly purchasing trends through visualizations created with Matplotlib, Seaborn, and Plotly. A Random Forest predictive model (Scikit-learn) was developed to explore purchase likelihood and customer behavior patterns. The entire workflow was managed using Git, GitHub, and Agile Kanban boards, ensuring clear tracking, documentation, and iterative development.

🎯 Objectives

Extract, clean, and merge multiple E-commerce datasets (Sales, Customers, Products)

Conduct Exploratory Data Analysis (EDA) to uncover behavioral insights

Visualize key trends using Matplotlib, Seaborn, and Plotly

Build a predictive model to estimate purchase probability

Apply Agile methodology for planning and documentation

Present findings through reports and presentations

📁 Repository Structure
ecommerce_project/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── main.py
├── ecommerce_Sales_Analysis.ipynb
│
├── customer_details.csv
├── product_details.csv
├── sales_data.csv
├── merged_ecommerce_data.csv
│
├── Ecommerce_Project_Report_Swathi.docx
└── Ecommerce_Project_Presentation_Swathi.pptx

⚙️ Technologies & Tools Used
Category	Tools / Libraries
Programming Language	Python 3.11
Data Manipulation	Pandas, NumPy
Visualization	Matplotlib, Seaborn, Plotly
Machine Learning	Scikit-learn (RandomForestClassifier)
Documentation	Jupyter Notebook, MS Word, PowerPoint
Project Management	GitHub Projects (Kanban), Agile Sprints

Workflow:
ETL → EDA → Product Insights → Predictive Modeling → Conclusions

🔄 ETL Pipeline Summary
Extract

Loaded CSV files from Kaggle

sales_data.csv

customer_data.csv

product_data.csv

Transform

Cleaned missing values and duplicates

Standardized timestamps and categorical variables

Merged datasets on unique keys (user_id, product_id)

Engineered features (e.g., is_purchase, month)

Load

Exported final data to merged_ecommerce_data.csv

Validation

Checked shapes, missing values, and logical consistency

📊 Data Analysis & Visualization
Key Insights

Customers aged 25–40 make the highest number of purchases

Digital payments (PayPal, Credit Card) dominate successful transactions

Top 10 products generate nearly 60% of total sales

Sales spike during Q4 (October–December)

Example Visualizations

Interaction Type Distribution
images/interaction_type_distribution.png

Customer Gender Distribution

images/pie_chart.png

Monthly Purchase Trend

images/monthly_purchase_trend.png

Feature Importance

images/feature_importance.png

📍 Visuals created using Matplotlib, Seaborn, and Plotly.

🤖 Predictive Modeling

Goal: Predict the likelihood of purchase

Model: Random Forest Classifier

Features:

Age

Gender

Payment Method

Frequency of Purchases

Target: is_purchase (1 = purchase, 0 = no purchase)

Accuracy: ~85%

Feature Importance Rank

Frequency of Purchases

Payment Method

Age

Gender

📊 Business Insights and Visualizations
1️⃣ Category Conversion Rate (Purchases / Views)
images/Category_conversion_rate.png

Insight: Footwear and Outerwear show the highest conversion rates.
Action: Prioritize stock and promotional spend on high-performing categories.

2️⃣ Average Order Value (AOV) by Payment Method
images/aov_by_payment_method.png
Insight: Debit Card and Bank Transfer users yield the highest AOV ($60–$62).
Action: Offer cashback / reward incentives for high-value payment channels.

3️⃣ Monthly Purchase Trend for Top Categories
images/monthly_purchase_trend.png
Insight: Sales peaks occur around March and September.
Action: Align marketing campaigns with seasonal demand patterns.

🎯 Customer Insights

Ages 25–40 dominate purchase activity

Digital payments → higher conversion

Engagement frequency = strongest predictor

🎯 Product Insights

Footwear & Outerwear → highest conversions

Accessories → high views but low conversions

Certain categories drive disproportionate revenue

💡 Recommendations

Promote high-performing categories with paid ads

Improve Accessories product pages (images, bundles)

Incentivize digital payments (card / PayPal)

Plan seasonal campaigns around peak months

Retarget high-frequency users

Build loyalty programs around digital wallet users

🧩 Agile Project Management

Managed using GitHub Projects (Kanban board)

Sprints included:

ETL

Visualizations

Modeling

Documentation

Daily reflection logs maintained

Roles practiced:

ETL Specialist

Visualization Analyst

Project Manager

🪞 Reflection & Learning
✔ Key Learnings

Built complete ETL pipeline using Python & Pandas

Improved skills in:

Pandas, NumPy

Matplotlib, Seaborn, Plotly

Machine learning (Scikit-learn)

Git/GitHub version control

Agile workflow

✔ Challenges

Handling missing data

Fixing timestamp inconsistencies

Merging large datasets

Balancing model accuracy & interpretability

✔ Future Enhancements

Deploy dashboard using Streamlit / Dash

Integrate marketing or regional datasets

Apply hyperparameter tuning

📚 References

Kaggle – E-commerce Sales Data 2024

Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn

Code Institute documentation

AI Assistance: Structure & visualization guidance

🌟 Acknowledgements

Special thanks to the Code Institute Faculty for guidance.

🌐 Connect With Me

👩‍💻 Swathi Mulkundkar
🔗 LinkedIn

💻 GitHub

⭐ Support

If you found this project helpful, please give it a star on GitHub! ⭐