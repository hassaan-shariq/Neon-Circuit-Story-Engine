import os
from groq import Groq, APIConnectionError, RateLimitError, APIStatusError
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
except Exception:
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)



class StoryEngine:
    def __init__(self):
        self.client = client
        self.model = "llama-3.1-8b-instant"
        self.universe_context = """You are a storyteller in the Neon Circuit universe — 
        a futuristic city where cars are alive, streets pulse with neon light, 
        and racing is the highest form of existence. Districts have names like 
        Nightshade, Voltspire, and Crimson Hollow. Cars have personalities, 
        rivalries, and legends. Stories are cinematic, fast, and vivid."""

    def generate_story(self, character_name, car_type):
        character_name = character_name.strip()
        car_type = car_type.strip()
        
        if not character_name or not character_name.strip():
            raise ValueError("Character name cannot be empty.")
        if not car_type or not car_type.strip():
            raise ValueError("Car type cannot be empty.")
        if len(character_name) > 50:
            raise ValueError("Character name is too long. Please limit to 50 characters.")
        if len(car_type) > 50:
            raise ValueError("Car type is too long. Please limit to 50 characters.")

        prompt = f"""Write a short 3-sentence racing story about {character_name}, 
        a {car_type} competing in the Neon Circuit. 
        Make it vivid, fast, and cinematic."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.universe_context},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.85
            )
            return response.choices[0].message.content

        
        except RateLimitError:
            raise RuntimeError("Rate limit exceeded. Please try again later.")
        except APIConnectionError:
            raise RuntimeError("Cannot connect to the API. Please check your internet connection.")
        except APIStatusError as e:
            raise RuntimeError(f"AI service error: {e.status_code}")
        except Exception as e:
            raise RuntimeError(f"Story generation failed: {str(e)}")
