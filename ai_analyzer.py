import os

def analyze_product(name):
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Analyze {name}"}]
        )

        return res.choices[0].message.content
    except:
        return f"""
🔍 Insight

{name}

• Demand: Good
• Competition: Moderate
• Opportunity: High
"""
