# Flying at the Speed of Sound: A Realtime AI Voice Experience for EGYPTAIR
I wanted to build a voice assistant that doesn't just "process" your requests, but actually *listens* and *responds* like a human. No more awkward pauses, no more robotic lag. Using **Google’s Gemini 2.5 Flash Realtime API** and **LiveKit**, I’ve created a seamless, low-latency voice experience for EGYPTAIR travelers.

---

###  The Experience
https://github.com/user-attachments/assets/bbeaef0f-0359-410b-ad27-ddcefb6487f0

---

###  The Evolution: Why I moved to Realtime
Before this, I built a [Traditional Voice Pipeline](https://github.com/MohamedTarekMostafa/EGYPTAIR-AI-Voice-Assistant). While it worked, it felt like a walkie-talkie. Here is why the **Realtime API** is a game-changer:

| Feature | [Traditional Pipeline (Old)](https://github.com/MohamedTarekMostafa/EGYPTAIR-AI-Voice-Assistant) | SkyTalk Realtime (Current) |
| :--- | :--- | :--- |
| **Feel** | Wait... think... talk (Robotic) | **Instant & Natural (Human)** |
| **Latency** | 3-5 Seconds | **< 1 Second** |
| **Brain** | 3 Separate Models (STT/LLM/TTS) | **Single Multimodal Brain** |
| **Context** | Pure Text Only | **Hears Tone, Pitch & Emotion** |

---

### What’s happening under the hood?
Standard bots use a "telephone game" architecture—converting your voice to text, then text to text, then text back to voice. This project skips the middleman:

* **Native Audio Intelligence:** The `gemini-2.5-flash-native-audio-preview` engine hears your voice directly. It understands "Umm," "Uh," and your mood.
* **Seamless Flow:** Powered by **LiveKit Agents**, the audio streams via WebRTC, allowing you to interrupt the assistant mid-sentence just like a real conversation.
* **Persona-Driven:** Designed specifically as a professional EGYPTAIR concierge—welcoming, helpful, and concise.

---

###  Getting Started
1.  **Clone & Install:**
    ```bash
    pip install livekit-agents livekit-plugins-google python-dotenv
    ```
2.  **Configuration:** Add your `GOOGLE_API_KEY`, `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` to a `.env` file.
3.  **Launch the Agent:**
    ```bash
    python main.py dev
    ```

---

### 🌍 What's next?
I’m working on connecting this assistant to live flight databases. Soon, it won't just talk—it will be able to rebook your flight or check your gate status in real-time.

---
*Built for a better travel experience. ✈️*




