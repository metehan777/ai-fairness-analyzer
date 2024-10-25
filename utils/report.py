import pandas as pd
import plotly.express as px

def generate_report(original_metrics, mitigated_dataset, mitigation_method):
    """
    Generate an HTML report comparing original and mitigated results
    """
    html_content = f"""
    <html>
    <head>
        <title>Fairness Analysis Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .metric {{ margin: 20px 0; padding: 10px; background: #f5f5f5; }}
        </style>
    </head>
    <body>
        <h1>Fairness Analysis Report</h1>
        <h2>Original Metrics</h2>
        <div class="metric">
            <h3>Demographic Parity: {original_metrics['demographic_parity']:.3f}</h3>
            <h3>Equal Opportunity: {original_metrics['equal_opportunity']:.3f}</h3>
            <h3>Disparate Impact: {original_metrics['disparate_impact']:.3f}</h3>
            <h3>Group Fairness: {original_metrics['group_fairness']:.3f}</h3>
        </div>
        
        <h2>Mitigation Applied: {mitigation_method}</h2>
        
        <h2>Recommendations</h2>
        <ul>
            <li>Consider additional data collection if disparate impact is high</li>
            <li>Review feature selection process</li>
            <li>Monitor metrics over time</li>
        </ul>
    </body>
    </html>
    """
    
    return html_content
