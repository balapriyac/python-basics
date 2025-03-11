# Standardize Your Data Import Process

def load_dataset(file_path, **kwargs):
    """
    Load data from various file formats while handling common issues.
    
    Args:
        file_path (str): Path to the data file
        **kwargs: Additional arguments to pass to the appropriate pandas reader
    
    Returns:
        pd.DataFrame: Loaded and initially processed dataframe
    """
    import pandas as pd
    from pathlib import Path
    
    file_type = Path(file_path).suffix.lower()
    
    # Dictionary of file handlers
    handlers = {
        '.csv': pd.read_csv,
        '.xlsx': pd.read_excel,
        '.json': pd.read_json,
        '.parquet': pd.read_parquet
    }
    
    # Get appropriate reader function
    reader = handlers.get(file_type)
    if reader is None:
        raise ValueError(f"Unsupported file type: {file_type}")
    
    # Load data with common cleaning parameters
    df = reader(file_path, **kwargs)
    
    # Initial cleaning steps
    df.columns = df.columns.str.strip().str.lower()  # Standardize column names
    df = df.replace('', pd.NA)  # Convert empty strings to NA
    
    return df


def validate_dataset(df, validation_rules=None):
    """
    Apply validation rules to a dataframe and return validation results.
    
    Args:
        df (pd.DataFrame): Input dataframe
        validation_rules (dict): Dictionary of column names and their validation rules
        
    Returns:
        dict: Validation results with issues found
    """
    if validation_rules is None:
        validation_rules = {
            'numeric_columns': {
                'check_type': 'numeric',
                'min_value': 0,
                'max_value': 1000000
            },
            'date_columns': {
                'check_type': 'date',
                'min_date': '2000-01-01',
                'max_date': '2025-12-31'
            }
        }

    validation_results = {}
    
    for column, rules in validation_rules.items():
        if column not in df.columns:
            continue
            
        issues = []
        
        # Check for missing values
        missing_count = df[column].isna().sum()
        if missing_count > 0:
            issues.append(f"Found {missing_count} missing values")
            
        # Type-specific validations
        if rules['check_type'] == 'numeric':
            if not pd.api.types.is_numeric_dtype(df[column]):
                issues.append("Column should be numeric")
            else:
                out_of_range = df[
                    (df[column] < rules['min_value']) | 
                    (df[column] > rules['max_value'])
                ]
                if len(out_of_range) > 0:
                    issues.append(f"Found {len(out_of_range)} values outside allowed range")
                    
        validation_results[column] = issues
    
    return validation_results
