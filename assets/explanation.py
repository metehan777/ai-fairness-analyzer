def get_metric_explanations():
    """
    Return explanations for each fairness metric
    """
    return {
        "Demographic Parity": """
        Demographic parity requires that the prediction is independent of the protected attribute. 
        A classifier satisfies this definition if subjects in both protected and unprotected groups 
        have equal probability of being assigned to the positive predicted class.
        """,
        
        "Equal Opportunity": """
        Equal opportunity requires that the true positive rates are similar across groups. 
        This means that individuals who qualify for a favorable outcome should have equal 
        probability of being correctly classified for this outcome, regardless of protected attributes.
        """,
        
        "Disparate Impact": """
        Disparate impact measures the ratio of favorable outcomes between unprivileged and privileged groups. 
        A value of 1.0 represents perfect fairness, while values below 0.8 or above 1.2 may indicate 
        discrimination according to the 80% rule used in US law.
        """,
        
        "Group Fairness": """
        Group fairness ensures that groups defined by protected attributes receive similar treatment. 
        It measures the extent to which different demographic groups are treated equally by the model 
        or dataset.
        """
    }
