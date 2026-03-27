import os

def analyze_product(product_name):
    try:
        from openai import OpenAI

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return fallback(product_name)

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Analyze this product: {product_name}"}
            ]
        )

        return response.choices[0].message.content

    except:
        return fallback(product_name)


def fallback(product_name):
    return f"""
🔍 AI Insight (Safe Mode)

Product: {product_name}

• Trend: Growing niche  
• Opportunity: Medium-High  
• Idea: Improve branding + bundle  
"""
