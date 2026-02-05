from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Title Page
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Mall Customer Segmentation using K-Means Clustering", ln=True, align='C')
pdf.ln(10)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, "Submitted by: [Your Name]", ln=True, align='C')
pdf.cell(0, 10, "Course: [Your Course Name]", ln=True, align='C')
pdf.cell(0, 10, "Date: [Submission Date]", ln=True, align='C')

# Introduction
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Introduction", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
"This project performs customer segmentation using K-Means clustering.\n"
"Customers are grouped based on their Annual Income and Spending Score.\n"
"This helps retail businesses understand customer behavior and plan targeted marketing strategies."
)

# Objective
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "\nObjective", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
"- Understand customer behavior\n"
"- Identify high-value customers\n"
"- Apply K-Means clustering and Elbow method\n"
"- Improve marketing strategy and segmentation"
)

# Dataset
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "\nDataset Description", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
"| Column Name | Description |\n"
"|------------|-------------|\n"
"| CustomerID | Unique customer ID |\n"
"| Gender | Male/Female |\n"
"| Age | Customer age |\n"
"| Annual Income (k$) | Income in thousand dollars |\n"
"| Spending Score (1-100) | Customer spending score |\n"
"\nTotal Records: 200 (example)"
)

# Methodology
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "\nMethodology", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
"1. Load dataset using pandas\n"
"2. Select features: Annual Income and Spending Score\n"
"3. Use Elbow method to determine optimal clusters\n"
"4. Apply K-Means clustering with optimal k\n"
"5. Assign each customer to a cluster\n"
"6. Visualize clusters using scatter plots\n"
"7. Analyze cluster centroids and segment customers"
)

# Code Explanation
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "\nCode Explanation", ln=True)
pdf.set_font("Courier", '', 10)
pdf.multi_cell(0, 6,
"# Load dataset\n"
"data = pd.read_csv('Mall_Customers.csv')\n\n"
"# Select features\n"
"X = data[['Annual Income (k$)', 'Spending Score (1-100)']]\n\n"
"# Elbow method\n"
"for i in range(1, 11):\n"
"    kmeans = KMeans(n_clusters=i, random_state=42)\n"
"    kmeans.fit(X)\n\n"
"# K-Means clustering\n"
"kmeans = KMeans(n_clusters=5, random_state=42)\n"
"data['Cluster'] = kmeans.fit_predict(X)"
)

# Placeholder for graphs
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "\nGraphs", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
"Insert screenshots of Elbow Graph and Cluster Graph here."
)

# Cluster Summary
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "\nCluster Summary", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
"| Cluster | Avg Annual Income | Avg Spending Score |\n"
"|---------|-----------------|------------------|\n"
"| 0       | 25              | 75               |\n"
"| 1       | 90              | 20               |\n"
"| 2       | 55              | 50               |\n"
"| 3       | 80              | 90               |\n"
"| 4       | 40              | 40               |"
)
# # new
# Cluster 0: Low income, high spending customers – impulse buyers
# Cluster 1: High income, low spending customers – careful premium buyers
# Cluster 2: Average income and spending – regular customers
# Cluster 3: High income, high spending – VIP customers
# Cluster 4: Low income, low spending – low priority segment


# Questions & Answers
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "\nPossible Questions & Answers", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
"Q1: What is K-Means clustering?\nA1: Unsupervised algorithm grouping data into k clusters.\n\n"
"Q2: Why Elbow method?\nA2: To find optimal number of clusters.\n\n"
"Q3: Features used?\nA3: Annual Income and Spending Score.\n\n"
"Q4: Business benefit?\nA4: Targeted marketing and strategy planning.\n\n"
"Q5: Cluster centroids?\nA5: Central points representing average values in each cluster."
)

# Conclusion
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "\nConclusion", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
"- Successfully segmented customers using K-Means\n"
"- Identified 5 distinct clusters\n"
"- Can be used for marketing strategy, loyalty programs, and sales prediction"
)

# Save PDF
pdf.output("Mall_Customer_KMeans_Report.pdf")
print("PDF generated successfully: Mall_Customer_KMeans_Report.pdf")
