from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Proxy API")


@app.get("/")
def read_root():
    return {"message": "LLM API with RunPod is running 🚀"}


@app.get("/get-country/{country}")
def get_country_data(country: str):
    """
    Example using another public API to fetch country information.
    """
    url = f"https://restcountries.com/v3.1/name/{country}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return {"status": "success", "country_data": data}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


