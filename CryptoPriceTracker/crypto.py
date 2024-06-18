from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get("/")
async def get_crypto_prices():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.coingecko.com/api/v3/coins/markets", params={"vs_currency": "usd"})
        return response.json()
