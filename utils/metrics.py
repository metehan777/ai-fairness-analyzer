from aif360.metrics import BinaryLabelDatasetMetric
import numpy as np

def calculate_fairness_metrics(dataset):
    """
    Calculate various fairness metrics for the dataset
    """
    metrics = {}
    
    # Initialize metric calculator
    dataset_metric = BinaryLabelDatasetMetric(dataset)
    
    # Demographic Parity
    metrics['demographic_parity'] = dataset_metric.statistical_parity_difference()
    
    # Equal Opportunity
    metrics['equal_opportunity'] = dataset_metric.equal_opportunity_difference()
    
    # Disparate Impact
    metrics['disparate_impact'] = dataset_metric.disparate_impact()
    
    # Group Fairness
    metrics['group_fairness'] = calculate_group_fairness(dataset)
    
    return metrics

def calculate_group_fairness(dataset):
    """
    Calculate group fairness metric
    """
    privileged_groups = [{dataset.protected_attribute_names[0]: 1}]
    unprivileged_groups = [{dataset.protected_attribute_names[0]: 0}]
    
    return dataset.disparate_impact(
        privileged_groups=privileged_groups,
        unprivileged_groups=unprivileged_groups
    )
