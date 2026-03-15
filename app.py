from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import httpx
import asyncio
import threading
import webbrowser
import time
import os
import signal
from platforms import PLATFORMS

app = FastAPI(title="OSINT Username Lookup")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


async def probe_platform(client: httpx.AsyncClient, platform: dict, username: str) -> dict:
    # Build URL — Tumblr uses subdomain, everything else uses {u} in path
    if platform["id"] == "tumblr":
        url = f"https://{username}.tumblr.com"
    else:
        url = platform["url"].replace("{u}", username)

    try:
        resp = await client.get(url, timeout=10.0, follow_redirects=True)

        method = platform["method"]

        if method == "status":
            status = "found" if resp.status_code == 200 else "miss"

        elif method == "body":
            if resp.status_code == 404:
                status = "miss"
            elif any(
                s.lower() in resp.text.lower()
                for s in platform.get("not_found_strings", [])
            ):
                status = "miss"
            else:
                status = "found"

        else:  # fallback
            status = "found" if resp.status_code == 200 else "miss"

        return {
            "id": platform["id"],
            "status": status,
            "url": url,
            "http_code": resp.status_code,
        }

    except httpx.TimeoutException:
        return {
            "id": platform["id"],
            "status": "error",
            "url": url,
            "http_code": None,
            "error": "Timeout",
        }
    except Exception as e:
        return {
            "id": platform["id"],
            "status": "error",
            "url": url,
            "http_code": None,
            "error": str(e),
        }


@app.get("/api/scan/{username}")
async def scan(username: str):
    async with httpx.AsyncClient(headers=HEADERS, follow_redirects=True) as client:
        tasks = [probe_platform(client, p, username) for p in PLATFORMS]
        results = await asyncio.gather(*tasks)

    platform_map = {p["id"]: p for p in PLATFORMS}
    enriched = []
    for r in results:
        p = platform_map.get(r["id"], {})
        enriched.append(
            {
                **r,
                "name": p.get("name", r["id"]),
                "icon": p.get("icon", ""),
                "cat": p.get("cat", ""),
            }
        )

    found_count = sum(1 for r in enriched if r["status"] == "found")
    miss_count = sum(1 for r in enriched if r["status"] == "miss")
    error_count = sum(1 for r in enriched if r["status"] == "error")

    return {
        "username": username,
        "results": enriched,
        "stats": {
            "found": found_count,
            "miss": miss_count,
            "error": error_count,
            "total": len(enriched),
        },
    }


@app.get("/api/quit")
async def quit_server():
    threading.Thread(target=lambda: (time.sleep(0.3), os.kill(os.getpid(), signal.SIGTERM)), daemon=True).start()
    return {"status": "bye"}


@app.get("/")
async def root():
    return FileResponse("static/index.html")


app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn

    def _open_browser():
        time.sleep(1.2)
        webbrowser.open("http://localhost:8000")

    threading.Thread(target=_open_browser, daemon=True).start()
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
