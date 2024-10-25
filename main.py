import streamlit as st
import pandas as pd
import numpy as np
from utils.metrics import calculate_fairness_metrics
from utils.visualizations import create_metric_plots
from utils.mitigation import apply_mitigation
from utils.report import generate_report
from assets.explanation import get_metric_explanations
import plotly.express as px
from aif360.datasets import BinaryLabelDataset

def main():
    st.set_page_config(page_title="Fairness Metrics Toolkit", layout="wide")
    
    st.title("🎯 Fairness Metrics Toolkit")
    st.markdown("""
    Analyze and mitigate bias in your datasets and ML models using various fairness metrics.
    Upload your dataset and explore different fairness measures.
    """)

    # File upload
    uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=['csv'])
    
    if uploaded_file is not None:
        # Load and prepare data
        df = pd.read_csv(uploaded_file)
        
        # Data configuration
        st.subheader("Dataset Configuration")
        target_column = st.selectbox("Select target variable", df.columns)
        protected_attribute = st.selectbox("Select protected attribute", df.columns)
        
        if st.button("Analyze Fairness"):
            # Convert to AIF360 format
            binary_label_dataset = BinaryLabelDataset(
                df=df,
                label_names=[target_column],
                protected_attribute_names=[protected_attribute]
            )
            
            # Calculate metrics
            metrics = calculate_fairness_metrics(binary_label_dataset)
            
            # Display results
            st.subheader("Fairness Metrics Results")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Demographic Parity", f"{metrics['demographic_parity']:.3f}")
                st.metric("Equal Opportunity", f"{metrics['equal_opportunity']:.3f}")
            
            with col2:
                st.metric("Disparate Impact", f"{metrics['disparate_impact']:.3f}")
                st.metric("Group Fairness", f"{metrics['group_fairness']:.3f}")
            
            # Visualizations
            st.subheader("Metric Visualizations")
            plots = create_metric_plots(binary_label_dataset, metrics)
            st.plotly_chart(plots['demographic_parity'])
            st.plotly_chart(plots['impact_plot'])
            
            # Mitigation options
            st.subheader("Bias Mitigation")
            mitigation_method = st.selectbox(
                "Select mitigation technique",
                ["Reweighing", "Disparate Impact Remover", "None"]
            )
            
            if mitigation_method != "None":
                mitigated_dataset = apply_mitigation(
                    binary_label_dataset,
                    mitigation_method
                )
                st.success("Mitigation applied successfully!")
                
                # Generate and download report
                if st.button("Generate Report"):
                    report = generate_report(
                        original_metrics=metrics,
                        mitigated_dataset=mitigated_dataset,
                        mitigation_method=mitigation_method
                    )
                    st.download_button(
                        "Download Report",
                        report,
                        file_name="fairness_report.html"
                    )
    
    # Display metric explanations
    with st.expander("📚 Understanding Fairness Metrics"):
        explanations = get_metric_explanations()
        for metric, explanation in explanations.items():
            st.markdown(f"### {metric}")
            st.write(explanation)

if __name__ == "__main__":
    main()
