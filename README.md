# **Data Fusion Project**

The **Data Fusion Project** is a Python-based pipeline designed to load, clean, and merge data from various formats into a unified dataset. This project handles multiple data sources, preprocesses the data to ensure consistency and quality, and produces a clean, merged CSV file for further analysis or usage.

---

## **Features**
- **Data Loading**: Supports multiple formats, including JSON, YAML, CSV, and XML.
- **Data Cleaning**: Removes invalid or redundant data, handles missing values, and normalizes columns.
- **Data Merging**: Combines data from various sources while maintaining consistency.
- **Output Persistence**: Saves the final unified dataset as a CSV file.

---

## **Project Structure**
The project is organized into modular Python scripts for scalability and readability:
- **`data_ingestion.py`**: Handles loading of data from various file formats.
- **`data_cleaning.py`**: Performs data preprocessing tasks such as cleaning, flattening nested structures, and handling missing values.
- **`data_merge.py`**: Implements the logic for merging datasets into a single, unified structure.
- **`data_persistence.py`**: Manages saving the unified dataset to a CSV file.
- **`main.py`**: Orchestrates the entire pipeline by invoking the required modules.

---

## **Dependencies**
To run this project, you will need:
- **Python 3.7+**
- Required Python packages (install using `pip`):
  ```bash
  pip install pandas pyyaml xmltodict
  ```

---

## **Usage**

The unified dataset will be saved as `unified_data.csv` in the project directory.

---

## **Main Workflow**

1. **Load Data**:  
   Reads files from various formats and converts them into Pandas DataFrames.

2. **Clean Data**:  
   Cleans and preprocesses data, including:
   - Flattening nested fields (e.g., locations).
   - Handling missing values in key columns.
   - Normalizing column data types.

3. **Merge Data**:  
   Combines all datasets into a single DataFrame.

4. **Save Data**:  
   Saves the unified DataFrame as `unified_data.csv`.

---

## **Example Input/Output**

### **Input Files**:
- `data/people.json`
- `data/people.yml`
- `data/promotions.csv`
- `data/transactions.xml`
- `data/transfers.csv`

### **Output**:
- `unified_data.csv`: A merged and cleaned dataset ready for analysis.

---

## **Future Improvements**

- Add support for additional data formats (e.g., Parquet, Excel).
- Implement more advanced missing value handling using imputation.
- Optimize merging logic for large-scale datasets.
- Include automated tests for validation and quality control.