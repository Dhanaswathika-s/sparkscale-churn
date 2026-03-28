Data Engineering Project using PySpark & Docker
📌 Overview
This project demonstrates a simple data pipeline using PySpark and Docker.
It reads a CSV file, performs basic transformations, and writes the output to a folder.

📁 Project Structure
Data-project/
│
├── docker-compose.yml
│
├── data/
│   ├── sample.csv
│   └── output/
│
└── scripts/
    ├── ingestion.py
    ├── transform.py
    └── output.py

    
⚙️ Technologies Used
1.Python
2.PySpark
3.Docker


🚀 Features
Reads CSV data using PySpark
Performs data transformation (filtering)
Saves processed data to output folder
Uses Docker for containerized execution


📄 Sample Data
id,name,age
1,John,25
2,Alice,30
3,Bob,22


🔄 Process Flow
Load data from CSV file
Apply transformation (filter age > 23)
Save output to data/output folder


📤 Output
The processed data is stored in:

data/output/

Files generated:

part-00000.csv
_SUCCESS

▶️ How to Run
Start Docker:
docker compose up -d
Run ingestion:
spark-submit /scripts/ingestion.py
Run transformation:
spark-submit /scripts/transform.py

✅ Result
Filtered data will be saved in the output folder.

📌 Author
Dhana Swathika

