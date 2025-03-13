import os
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from deepgram import DeepgramClient

# Load API Key
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
deepgram = DeepgramClient(DEEPGRAM_API_KEY)

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # Initialize Deepgram live transcription
    connection = deepgram.transcription.live({
        "punctuate": True,
        "interim_results": True,
        "language": "en",
    })

    async def deepgram_handler():
        async for data in connection:
            transcript = data.get("channel", {}).get("alternatives", [{}])[0].get("transcript", "")
            if transcript:
                await websocket.send_text(transcript)  # Send transcript to frontend

    deepgram_task = asyncio.create_task(deepgram_handler())

    try:
        while True:
            audio_data = await websocket.receive_bytes()  # Receive audio from Twilio
            await connection.send(audio_data)  # Send it to Deepgram
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await connection.close()
        deepgram_task.cancel()
