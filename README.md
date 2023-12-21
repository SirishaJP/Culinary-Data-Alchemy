# Data-Driven Insights for Seasonal Menu Alchemy: Profits, Segmentation, Trends, and Testing

The culinary domain, especially in the context of seasonal menu curation, is increasingly defined by data-driven precision and innovation. In this comprehensive project, we embark on an in-depth exploration of a hypothetical restaurant enterprise, where the primary objective is to achieve the pinnacle of menu optimization. Our journey spans a rich landscape of sophisticated data analyses, including profitability assessments, customer segmentation, time series investigations, robust A/B testing and Optimizing Shift Scheduling. Through advanced data science methodologies, we aim to extract profound insights and refine the art of Seasonal Menu Alchemy.

## Analysis 1: Profitability Analysis

**Objective**: To identify high-profit menu items via rigorous cost analysis and optimized pricing strategies.

**Methodology**: Our exploration begins with a meticulous examination of cost prices and selling prices, where we calculate profits using the formula:

             Profit = (Selling Price - Cost Price) * Quantity Sold


**Results**: Through this analytical prism, the **Avocado Chicken Bowl** emerges as a standout, commanding a selling price of € 12.50, yielding a substantial total profit of € 1,125.00. It's an exemplary case of menu engineering that significantly contributes to the restaurant's bottom line.

<img width="963" alt="Screenshot 2023-10-15 at 18 03 20" src="https://github.com/SirishaJP/Culinary-Data-Alchemy/assets/104147973/dbff4e2b-153b-4ead-971e-da06a6ea77a3">


## Analysis 2: Customer Segmentation

**Objective**: To categorize patrons into distinct segments, defined by demographic and spending characteristics, enabling tailored marketing strategies.

**Methodology**: Employing K-Means clustering, we employ a feature selection process, focusing on age and expenditure as essential attributes. Subsequently, we employ data scaling to ensure a balanced approach.

**Results**: The outcomes of our segmentation reveal three primary customer segments, each offering a unique lens into patronage. We distinguish:

- **Segment 0 (Low Spend Customers)**: With an average age of 30, they contribute an average of € 22 to the restaurant's revenue.
- **Segment 1 (Medium Spend Customers)**: An older demographic with an average age of 40, this group provides an average spending of € 30.
- **Segment 2 (High Spend Customers)**: With an average age of 48, this demographic yields a substantial average spending of € 40.

<img width="647" alt="Screenshot 2023-10-15 at 18 04 00" src="https://github.com/SirishaJP/Culinary-Data-Alchemy/assets/104147973/eeb7f6c9-8b45-49e5-bb37-5a38f2263288">


## Analysis 3: Time Series Trends

**Objective**: To decode temporal trends in sales and customer count, furnishing insights for optimized resource allocation.

**Methodology**: Our time series analysis leverages advanced data visualization techniques, unveiling intricate seasonal patterns. Mathematical modeling and statistical analysis play a central role in pattern recognition and forecasting.

**Results**: Our findings uncover the cyclicality of sales and customer counts, culminating in peak performances during the winter months. These temporal insights offer a roadmap for resource allocation optimization.

<img width="920" alt="Screenshot 2023-10-15 at 18 04 24" src="https://github.com/SirishaJP/Culinary-Data-Alchemy/assets/104147973/2872588a-9dfb-4f99-9fc2-8ff0ca4f06a2">



## Analysis 4: A/B Testing (T-Test)

**Objective**: To empirically validate the impact of menu changes on sales, underpinned by statistical rigor.

**Methodology**: In the tradition of hypothesis testing, we frame a null hypothesis (H0) positing no significant difference in sales between the old menu (Group A) and the new warm menu (Group B). A t-test is employed to rigorously analyze the total revenue of these groups.

**Results**: Our t-test yields a t-statistic of -2.4305594055372253 and a p-value of 0.031700105639650575. In the realm of statistics, these results unequivocally lead to the rejection of the null hypothesis (H0). The new warm menu (Group B) unmistakably outperforms the old menu (Group A) in terms of sales.

<img width="790" alt="Screenshot 2023-10-15 at 18 04 44" src="https://github.com/SirishaJP/Culinary-Data-Alchemy/assets/104147973/43a3aa91-080f-4e91-8477-1506e2c20b80">

## Analysis 5:  Automating Employee's Shift Scheduling 

**Objective** In today's fast-paced business environment, efficient scheduling is crucial. The use of data science in scheduling, particularly for staffing in industries like hospitality, healthcare, and retail, brings a new level of precision and optimization. Data science-driven scheduling systems analyze vast amounts of data to make informed decisions, balancing employee preferences, legal constraints, and organizational needs.

**Methodology: Incorporating Constraints and Preferences**

#### Employee Preferences

Personalized Schedules: By taking into account employee availability and preferences (e.g., preferred shifts, days off), the system fosters a more satisfied and productive workforce.

Fair Allocation: Data-driven algorithms ensure fair distribution of desirable and less desirable shifts, reducing potential conflicts and improving morale.

#### Scheduling Limitations

Legal Compliance: The system adheres to legal constraints, such as mandatory rest periods and maximum working hours, thus avoiding potential legal issues.

Operational Efficiency: By considering factors like peak hours, required skill sets, and shift overlaps, the system optimizes for efficient operations.

#### Company Requirements

Customization: The system can be tailored to accommodate specific company policies or operational needs, such as minimum staffing levels or special events.

Adaptability: It can quickly adapt to changes, like sudden employee absences or fluctuating demand, maintaining operational continuity.

####  Advantages of Using This System

Optimized Staffing: Ensures the right number of employees with the right skills are scheduled at the right times.
Time and Cost Efficiency: Reduces the administrative burden of manual scheduling, leading to cost savings.
Employee Satisfaction: Respects employee preferences and promotes work-life balance, leading to lower turnover rates.
Data-Driven Decisions: Leverages historical data for forecasting and planning, improving overall decision-making.
Scalability: Easily scales to accommodate business growth or seasonal fluctuations.

#### Technical Rationale for Using Linear Programming

Linear programming (LP) is ideal for scheduling due to its efficiency in handling large-scale, complex problems with multiple constraints. It offers several technical advantages:

Optimization: LP finds the most efficient solution that satisfies all given constraints, ensuring optimal resource allocation.

Flexibility: Can accommodate various types of constraints (e.g., availability, shift lengths, legal requirements).

Scalability: Efficiently handles large numbers of variables, making it suitable for businesses of all sizes.

Predictability: Provides consistent, repeatable outcomes, essential for operational planning.

**Result**

The final scheduling code effectively balanced employee preferences with operational needs, creating an optimized weekly roster that ensures each shift is adequately staffed. This result demonstrates the power of data-driven scheduling in enhancing both operational efficiency and employee satisfaction.

![Figure_1](https://github.com/SirishaJP/Culinary-Data-Alchemy/assets/104147973/abcb831d-af79-49d2-97a7-cbee5a4a898d)


## Conclusion

The data-driven journey encapsulated in this project, under the banner of Seasonal Menu Alchemy, is a testament to the power of mathematical precision and analytical acumen. Our exploration of profitability, customer segmentation, time series trends, and A/B testing provides profound insights for restaurant management.

Note: The data employed in this project is entirely hypothetical, designed to ensure privacy and data security.

In the realm of Seasonal Menu Alchemy, we witness the harmonious fusion of data science and culinary artistry, where analytics guides decision-making and elevates the dining experience to new heights. This synergy not only enhances operational efficiency but also tailors the culinary experience to meet evolving customer preferences. By integrating linear programming in employee scheduling, we've optimized workforce management, ensuring that every meal is crafted by the ideal team at the perfect moment. This project stands as a beacon, showcasing the limitless possibilities when data science is applied thoughtfully in the culinary world, paving the way for future innovations that blend technology with the art of gastronomy.
