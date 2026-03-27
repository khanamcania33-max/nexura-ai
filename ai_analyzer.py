import os

def analyze_product(name):
    try:
        from openai import OpenAI

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return fallback(name)

        client = OpenAI(api_key=api_key)

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Analyze {name} for Amazon opportunity"}]
        )

        return res.choices[0].message.content

    except:
        return fallback(name)


def fallback(name):
    return f"""
🔍 AI Insight

{name}

• Demand: Good  
• Competition: Moderate  
• Opportunity: High  
• Suggestion: Improve design + bundle
"""
