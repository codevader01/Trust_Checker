from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# CORS middleware for Chrome extension access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/rating/{domain}")
async def get_trustpilot_rating(domain: str):
    try:
        url = f"https://www.trustpilot.com/review/{domain}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return {"rating": "No rating found"}

        soup = BeautifulSoup(response.text, "html.parser")
        # Target the specific h4 element with class "typography_heading-xxs__UmE9o"
        rating_element = soup.find("h4", class_="typography_heading-xxs__UmE9o")
        rating = rating_element.get_text(strip=True) if rating_element else "No rating found"
        
        return {"rating": rating}
    except Exception:
        return {"rating": "No rating found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)