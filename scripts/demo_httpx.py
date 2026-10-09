import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/health")
        print(response.status_code)
        print(response.json())

if __name__ == "__main__":
    asyncio.run(main())
