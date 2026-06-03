def customer_segment(balance):

    if balance > 100000:
        return "High Value"

    elif balance > 50000:
        return "Medium Value"

    else:
        return "Mass Market"
    
def next_best_action(probability, balance, products, active_member):

    if probability >= 0.70:

        return (
            "High Churn Risk",
            "Retention Campaign",
            "High probability of churn detected. Prioritize proactive outreach."
        )

    elif products == 1:

        return (
            "Growth Opportunity",
            "Cross-Sell Banking Products",
            "Customer only uses one product. Opportunity to increase engagement."
        )

    elif balance > 100000:

        return (
            "High Value Customer",
            "Relationship Manager Engagement",
            "High-value customer requiring personalized service."
        )

    else:

        return (
            "Stable Customer",
            "Maintain Engagement",
            "Continue personalized communication and monitoring."
        )