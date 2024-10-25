from aif360.algorithms.preprocessing import Reweighing, DisparateImpactRemover

def apply_mitigation(dataset, method):
    """
    Apply bias mitigation technique to the dataset
    """
    if method == "Reweighing":
        mitigator = Reweighing(
            unprivileged_groups=[{dataset.protected_attribute_names[0]: 0}],
            privileged_groups=[{dataset.protected_attribute_names[0]: 1}]
        )
        return mitigator.fit_transform(dataset)
    
    elif method == "Disparate Impact Remover":
        mitigator = DisparateImpactRemover(
            repair_level=1.0,
            sensitive_attribute=dataset.protected_attribute_names[0]
        )
        return mitigator.fit_transform(dataset)
    
    return dataset
