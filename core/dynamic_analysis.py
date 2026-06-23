import re
from core.config_loader import CONFIG

def parse_filters(question):

    question = question.lower()
    filters = {}
    

    for column_name, mappings in CONFIG["filters"].items():
        for db_value, synonyms in mappings.items():
            pattern = r"\b(" + "|".join(synonyms) + r")\b"
            
            if re.search(pattern, question):
                if db_value.isdigit():
                    filters[column_name] = int(db_value)
                else:
                    filters[column_name] = db_value

    return filters

def apply_filters(df, filters):
    filtered_df = df.copy()
    for key, value in filters.items():
        if key in filtered_df.columns:
            filtered_df = filtered_df[filtered_df[key] == value]
    return filtered_df

def compute_dynamic_stats(df):
    if len(df) == 0:
        return None

    target_col = CONFIG["dataset"]["target_column"]
    attendance = df[target_col].mean()
    no_show = 1 - attendance

    return {
        "attendance": attendance,
        "no_show": no_show,
        "count": len(df)
    }