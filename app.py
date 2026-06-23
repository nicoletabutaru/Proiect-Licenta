from flask import Flask, request, render_template, jsonify
from core.data_loader import load_data
from core.statistics_engine import build_statistics_dict
from core.retriever import Retriever
from core.response_generator import generate_response
from core.visualizer import plot_bar, plot_dynamic_comparison
from core.dynamic_analysis import parse_filters, apply_filters, compute_dynamic_stats
from core.config_loader import CONFIG


from core.history_manager import init_db, save_interaction, get_history

app = Flask(__name__)


df = load_data()
stats = build_statistics_dict(df)
retriever = Retriever()


init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    if not question:
        return {"answer": "Please provide a question.", "img": None}

    filters = parse_filters(question)

    
    if len(filters) >= 2:
        filtered_df = apply_filters(df, filters)
        dynamic_stats = compute_dynamic_stats(filtered_df)

        if dynamic_stats is None or dynamic_stats["count"] == 0:
            answer = "No data found for these combined criteria."
            save_interaction(question, "Multi-Filter (No Data)", answer)
            return {"answer": answer, "img": None}

        answer = (f"Based on {dynamic_stats['count']} records matching your criteria, "
                  f"the target rate is {dynamic_stats['attendance']*100:.2f}%.")
        
        img_base64 = plot_dynamic_comparison(dynamic_stats, stats["overall"])
        
        save_interaction(question, "Dynamic Drill-Down", answer)
        
        return {"answer": answer, "img": img_base64}

  
    topic = retriever.get_topic(question)
    answer = generate_response(topic, stats, question)
    img_base64 = plot_bar(stats, topic)

   
    save_interaction(question, topic, answer)

    return {"answer": answer, "img": img_base64}


@app.route("/history_api", methods=["GET"])
def history_api():
    logs = get_history()
    history_list = [{"timestamp": row[0], "question": row[1], "topic": row[2], "response": row[3]} for row in logs]
    return jsonify(history_list)

if __name__ == "__main__":
    app.run(debug=True)