import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

print(f"DEBUG - Key: {os.getenv('GROQ_API_KEY')}")
print(f"DEBUG - .env path: {os.path.abspath('.env')}")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_neon_story(character_name, car_type):
    prompt = f"""You are a storyteller in the Neon Circuit universe — 
    a futuristic city where cars are alive and districts pulse with neon light.
    
    Write a short 3-sentence story about {character_name}, 
    a {car_type} who races through the Neon Circuit.
    Make it vivid, fast, and cinematic."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a creative storyteller for the Neon Circuit universe."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=150,
        temperature=0.8
    )

    return response.choices[0].message.content


def main():
    print("=== NEON CIRCUIT STORY ENGINE ===\n")
    character_name = input("Enter character name: ").strip()
    car_type = input("Enter car type: ").strip()
    print("\nGenerating your story...\n")
    story = generate_neon_story(character_name, car_type)
    print(story)


if __name__ == "__main__":
    main()