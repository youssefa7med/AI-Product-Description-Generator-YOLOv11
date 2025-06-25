import os
import uuid
import random
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from urllib.request import urlretrieve
from ultralytics import YOLO
from gtts import gTTS
from dotenv import load_dotenv
from PIL import Image
from fastapi.responses import JSONResponse
import re

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    raise EnvironmentError("Missing DEEPSEEK_API_KEY in environment.")
os.environ['DEEPSEEK_API_KEY'] = DEEPSEEK_API_KEY

model = YOLO("best.pt")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists("audio"):
    os.makedirs("audio")
app.mount("/audio", StaticFiles(directory="audio"), name="audio")

class ImageURL(BaseModel):
    url: str
    name: str | None = None
    language: str = "English"

LANGUAGE_TO_GTTS = {
    'Afrikaans': 'af', 'Amharic': 'am', 'Arabic': 'ar', 'Bulgarian': 'bg', 'Bengali': 'bn', 'Bosnian': 'bs',
    'Catalan': 'ca', 'Czech': 'cs', 'Welsh': 'cy', 'Danish': 'da', 'German': 'de', 'Greek': 'el', 'English': 'en',
    'Spanish': 'es', 'Estonian': 'et', 'Basque': 'eu', 'Finnish': 'fi', 'French': 'fr', 'French (Canada)': 'fr-CA',
    'Galician': 'gl', 'Gujarati': 'gu', 'Hausa': 'ha', 'Hindi': 'hi', 'Croatian': 'hr', 'Hungarian': 'hu',
    'Indonesian': 'id', 'Icelandic': 'is', 'Italian': 'it', 'Hebrew': 'iw', 'Japanese': 'ja', 'Javanese': 'jw',
    'Khmer': 'km', 'Kannada': 'kn', 'Korean': 'ko', 'Latin': 'la', 'Lithuanian': 'lt', 'Latvian': 'lv',
    'Malayalam': 'ml', 'Marathi': 'mr', 'Malay': 'ms', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Dutch': 'nl',
    'Norwegian': 'no', 'Punjabi (Gurmukhi)': 'pa', 'Polish': 'pl', 'Portuguese (Brazil)': 'pt',
    'Portuguese (Portugal)': 'pt-PT', 'Romanian': 'ro', 'Russian': 'ru', 'Sinhala': 'si', 'Slovak': 'sk',
    'Albanian': 'sq', 'Serbian': 'sr', 'Sundanese': 'su', 'Swedish': 'sv', 'Swahili': 'sw', 'Tamil': 'ta',
    'Telugu': 'te', 'Thai': 'th', 'Filipino': 'tl', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur',
    'Vietnamese': 'vi', 'Cantonese': 'yue', 'Chinese (Simplified)': 'zh-CN', 'Chinese (Mandarin/Taiwan)': 'zh-TW',
    'Chinese (Mandarin)': 'zh'
}

def get_gtts_lang_code(language_name: str) -> str:
    return LANGUAGE_TO_GTTS.get(language_name, "en")

def predict_category(image_path: str) -> str:
    image = Image.open(image_path).convert("RGB")
    results = model(image)
    result = results[0]
    if result.boxes.cls.numel() == 0:
        return "No object detected"
    cls_id = int(result.boxes.cls[0])
    return model.names[cls_id]

def generate_description(name, category, lang):
    prompt = f"""
    Write a professional product description in {lang} for:
    - Product Name: {name if name else 'a ' + category}
    - Product Category: {category}

    Requirements:
    1. Start directly with the description (no introductions like "Here is...")
    2. Keep it between 30-50 words
    3. Use simple, clear language
    4. Focus on key features and benefits
    5. Do not include any greetings or sign-offs
    6. Format as a single paragraph without HTML tags

    Example format for English:
    "This {category} is designed for... It features... Ideal for..."
    """
    
    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
            json={
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a professional product description writer. Provide concise, direct descriptions without any introductory phrases."
                    },
                    {
                        "role": "user",
                        "content": prompt.strip()
                    }
                ],
                "temperature": random.uniform(0.9,1),
                "max_tokens": 1000,
            }
        )
        
        content = response.json()["choices"][0]["message"]["content"]
        cleaned_content = re.sub(r'^["\']|["\']$', '', content).strip()
        
        return cleaned_content
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API error: {str(e)}")
def text_to_speech(message: str, language: str) -> str:
    clean_text = re.sub(r'<[^>]+>', '', message)
    clean_text = clean_text.lstrip().replace("\n", " ")
    
    lang_code = get_gtts_lang_code(language)
    filename = f"audio/audio_{uuid.uuid4().hex}.mp3"
    
    if len(clean_text) > 500:
        clean_text = clean_text[:500] + "..."

    try:
        tts = gTTS(text=clean_text, lang=lang_code, slow=False)
        tts.save(filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text-to-speech error: {str(e)}")

    return filename

@app.post("/product/url/")
async def product_description_from_url(data: ImageURL):
    try:
        temp_filename = f"temp_{uuid.uuid4().hex}.jpg"
        urlretrieve(data.url, temp_filename)

        category = predict_category(temp_filename)
        if category == "No object detected":
            os.remove(temp_filename)
            raise HTTPException(status_code=400, detail="No recognizable product found in the image.")

        description = generate_description(name=data.name, category=category, lang=data.language)

        audio_path = text_to_speech(description, data.language)

        os.remove(temp_filename)

        return JSONResponse(content={
            "category": category,
            "description": description,
            "audio_path": f"/{audio_path}"
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
