from core.config_loader import CONFIG

def build_statistics_dict(df):
   
    stats = {}
    target_col = CONFIG["dataset"]["target_column"]

    overall_mean = df[target_col].mean()
    stats["overall"] = {
        "attendance": round(overall_mean, 4),
        "no_show": round(1 - overall_mean, 4)
    }


    for config_col in CONFIG["filters"].keys():
        if config_col in df.columns:
            topic_key = config_col.lower() 
            if topic_key == "hipertension": topic_key = "hypertension" 
            
            group_stats = df.groupby(config_col)[target_col].mean()
            stats[topic_key] = {str(k): round(v, 4) for k, v in group_stats.items()}


    if "SMS_received" in df.columns:
        sms_stats = df.groupby("SMS_received")[target_col].mean()
        stats["sms"] = {
            "received": round(sms_stats.get(1, 0), 4),
            "not_received": round(sms_stats.get(0, 0), 4)
        }


    return stats