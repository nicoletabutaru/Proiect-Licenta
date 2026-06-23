import matplotlib.pyplot as plt
import io
import base64

def _style_modern_ax(ax, title, ylabel):
    ax.set_title(title, pad=25, fontsize=14, fontweight='600', color='#1A2A3A', fontfamily='sans-serif')
    ax.set_ylabel(ylabel, fontsize=11, fontweight='500', color='#6B7280', fontfamily='sans-serif', labelpad=10)
    for spine in ax.spines.values(): 
        spine.set_visible(False)
    ax.tick_params(axis='x', colors='#4B5563', labelsize=10, pad=10)
    ax.tick_params(axis='y', colors='#6B7280', labelsize=10, length=0, pad=10)
    ax.yaxis.grid(True, linestyle='-', alpha=0.3, color='#E5E7EB')
    ax.set_axisbelow(True)

def _add_value_labels(ax):
    for p in ax.patches:
        ax.annotate(f"{p.get_height():.1f}%", 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10, color='#1A2A3A', fontweight='600',
                    xytext=(0, 8), textcoords='offset points')

def plot_dynamic_comparison(dynamic_stats, overall_stats):
    labels = ["Selected Group", "Overall Population"]
    values = [dynamic_stats["attendance"] * 100, overall_stats["attendance"] * 100]

   
    fig, ax = plt.subplots(figsize=(6, 4.2), dpi=140)
    ax.bar(labels, values, color=['#004B91', '#D1D5DB'], width=0.45, edgecolor='none')
    
    _style_modern_ax(ax, "Group Comparison", "Rate (%)")
    _add_value_labels(ax)
    ax.set_ylim(0, max(values) + 15)

    img = io.BytesIO()

    plt.savefig(img, format='png', bbox_inches='tight', transparent=True)
    img.seek(0)
    plt.close()
    return base64.b64encode(img.getvalue()).decode()

def plot_bar(stats, topic):
    if topic not in stats or topic == "overall": 
        return None

    labels = list(stats[topic].keys())
    labels = ["With" if l == "1" else "Without" if l == "0" else l for l in labels]
    values_pct = [v * 100 for v in stats[topic].values()]

    fig, ax = plt.subplots(figsize=(6, 4.2), dpi=140)
    ax.bar(labels, values_pct, color="#10B981", width=0.45, edgecolor='none')
    
    formatted_topic = topic.replace('_', ' ').title()
    _style_modern_ax(ax, f"Statistics: {formatted_topic}", "Rate (%)")
    _add_value_labels(ax)
    ax.set_ylim(0, max(values_pct) + 15)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight', transparent=True)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    plt.close()
    
    return img_base64