from core.config_loader import CONFIG

def interpret_difference(val1, val2):
    diff = abs(val1 - val2) * 100
    if diff < 2: return diff, "a negligible difference"
    elif diff < 5: return diff, "a slight difference"
    elif diff < 10: return diff, "a moderate difference"
    else: return diff, "a significant difference"

def generate_response(topic, stats, question=""):

    if topic not in stats and topic != "overall":
        return "I'm sorry, I don't have enough data to explain this specific topic yet."

    target_name = CONFIG["dataset"]["target_column"].lower()
    
  
    if topic == "overall":
        attend = stats["overall"]["attendance"] * 100
        return f"The overall {target_name} rate for this dataset is {attend:.2f}%."

    
    category_data = stats[topic]
    
   
    parts = []
    for key, rate in category_data.items():
       
        friendly_key = "With" if key == "1" else "Without" if key == "0" else key
        parts.append(f"{friendly_key}: {rate*100:.2f}%")
        
    main_text = f"Statistics for {topic.replace('_', ' ')}:\n" + " | ".join(parts) + "."

    
    reasoning_text = CONFIG["reasoning"].get(topic, "")
    if reasoning_text:
        main_text += f"\n\n💡 {reasoning_text}"

    return main_text