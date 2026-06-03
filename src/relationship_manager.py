def relationship_manager_brief(
    segment,
    churn_risk,
    balance,
    products,
    active_member
):

    brief = f"""
Customer Summary

Segment: {segment}

Churn Risk: {churn_risk:.0%}

Balance: {balance:,.0f}

Products Held: {products}

Recommended Action:
Relationship Manager Outreach

Suggested Conversation

Discuss customer financial goals,
understand service concerns,
and explore relevant banking products.
"""

    return brief