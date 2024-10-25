import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_metric_plots(dataset, metrics):
    """
    Create visualization plots for fairness metrics
    """
    plots = {}
    
    # Demographic Parity visualization
    df = pd.DataFrame({
        'Group': ['Privileged', 'Unprivileged'],
        'Positive Outcome Rate': [
            dataset.privileged_group_metadata()[0],
            dataset.unprivileged_group_metadata()[0]
        ]
    })
    
    plots['demographic_parity'] = px.bar(
        df,
        x='Group',
        y='Positive Outcome Rate',
        title='Demographic Parity Comparison',
        template='plotly_white'
    )
    
    # Impact visualization
    plots['impact_plot'] = go.Figure()
    plots['impact_plot'].add_trace(
        go.Indicator(
            mode="gauge+number",
            value=metrics['disparate_impact'],
            title={'text': "Disparate Impact"},
            gauge={'axis': {'range': [0, 2]},
                  'steps': [
                      {'range': [0, 0.8], 'color': "red"},
                      {'range': [0.8, 1.2], 'color': "green"},
                      {'range': [1.2, 2], 'color': "red"}
                  ],
                  'threshold': {
                      'line': {'color': "black", 'width': 4},
                      'thickness': 0.75,
                      'value': 1
                  }}
        )
    )
    
    return plots
