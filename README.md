# YouTube API Data Collection and ETL Pipeline

## Overview
This is a **Data Engineering Project** that involves collecting data from the **YouTube API** using an API key. The data is then processed using an ETL pipeline written in Python, where the data is extracted, transformed, and loaded into a **CSV file**. The project includes the integration of **Apache Airflow** to automate the ETL process, with the resulting CSV file being saved into an **AWS S3 bucket**. The entire pipeline is set up on **EC2** instances for execution and monitoring.

## Project Workflow


![YouTube API ETL Workflow](https://github.com/praveenreddy82472/DeProject_YoutubeAPI/blob/main/images/Flow.png)


1. **Collect Data from YouTube API:**
   - The project uses the YouTube Data API (v3) to collect data such as video details, comments, and other relevant metadata based on specified queries or channels.
   - A **Python function** is written to call the YouTube API and collect data using an API key.

2. **ETL Pipeline:**
   - **Extract:** The Python function pulls data from the YouTube API.
   - **Transform:** The data is cleaned and transformed (e.g., converting timestamps, formatting fields, filtering relevant columns).
   - **Load:** The transformed data is written to a CSV file, which will be later stored in S3.

3. **Automate ETL Process with Apache Airflow:**
   - An **Airflow DAG (Directed Acyclic Graph)** is created to trigger the ETL process at defined intervals.
   - The DAG manages the execution of the Python functions, ensuring the timely execution of the ETL pipeline.

4. **Store Data in AWS S3:**
   - After the ETL process, the resulting CSV file is saved to an **S3 bucket** for storage and further use.
   - This ensures that the data is easily accessible for analytics or further processing.

5. **Infrastructure on AWS EC2:**
   - The pipeline runs on an **EC2 instance**, which provides the necessary compute resources to execute the ETL pipeline and Airflow tasks.

## Key Components

- **YouTube API:** Collects video and comment data from YouTube.
- **Python (ETL script):** Extracts, transforms, and loads the data into a CSV file.
- **Apache Airflow:** Automates the execution of the ETL pipeline with a DAG.
- **AWS S3:** Stores the resulting data for further processing or analysis.
- **AWS EC2:** Hosts the execution environment for the Airflow tasks and Python scripts.

## Project Setup

### Prerequisites

- Python 3.x
- Apache Airflow
- AWS Account (for EC2 and S3)
- YouTube API Key
- Boto3 (for AWS interactions)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-github-username>/DeProject_YoutubeAPI.git
