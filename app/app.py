from flask import Flask, render_template, request
import pandas as pd
import joblib
import os
import sys

# Ensure the scripts directory is in the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

# Import functions from scripts
from visualizations import plot_sentiment_trends, plot_trading_signals, plot_strategy_returns
from reporting import generate_report

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    # Load the report
    try:
        with open('reports/summary_report.txt', 'r') as file:
            report_text = file.read()
    except FileNotFoundError:
        report_text = "No report found."

    # Render the index page with the report
    return render_template('index.html', report=report_text)

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Results Page
@app.route('/results', methods=['GET'])
def results():
    # Load financial news sentiment data
    try:
        df = pd.read_csv('data/processed/backtest_results.csv')
    except FileNotFoundError:
        return "Error: backtest_results.csv file not found.", 500

    # Load trained model
    try:
        model = joblib.load('models/trained_model.pkl')
    except FileNotFoundError:
        return "Error: trained_model.pkl file not found.", 500

    # Predict signals and update the dataframe
    df['predicted_signal'] = model.predict(df[['sentiment_score']])

    # Generate plots
    plot_sentiment_trends(df)
    plot_trading_signals(df)
    plot_strategy_returns(df)

    # Generate report
    try:
        generate_report('data/processed/backtest_results.csv', 'reports/summary_report.txt')
    except Exception as e:
        return f"Error generating report: {e}", 500

    # Send data to results page
    return render_template('results.html', report=df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
