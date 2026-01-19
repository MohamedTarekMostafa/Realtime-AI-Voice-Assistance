# Flying at the Speed of Sound: A Realtime AI Voice Experience for EGYPTAIR

This project is an exploration of what's possible when you combine **Google’s Gemini 2.5 Flash Realtime API** with **LiveKit**. I’ve built a voice concierge for EGYPTAIR that processes audio natively—meaning it hears, thinks, and speaks in real-time without the lag of traditional "speech-to-text" loops.

---

### 📺 The Demo
https://github.com/user-attachments/assets/bbeaef0f-0359-410b-ad27-ddcefb6487f0

> *Watch how the Realtime API handles natural interruptions and emotional cues.*

---

### 🚀 The Evolution: Pipeline vs. Realtime API

Before this version, I built a version using the traditional **Sequential Pipeline** (STT -> LLM -> TTS). Transitioning to the **Gemini 2.5 Realtime API** changed the game.

| Feature | [Traditional Pipeline]([YOUR_PIPELINE_REPO_LINK_HERE](https://github.com/MohamedTarekMostafa/Realtime-AI-Voice-Assistance)) | SkyTalk (Realtime API) |
| :--- | :--- | :--- |
| **Architecture** | 3 Separate Models (Delayed) | **End-to-End Native Audio** |
| **Latency** | 3-5 Seconds (Robotic) | **< 1 Second (Human-like)** |
| **Nuance** | Pure Text Only | **Understands Tone & Emotion** |
| **Flow** | Wait-to-talk (Walkie-talkie style) | **Seamless Interruptions** |

> **Check out the old version here:** [EGYPTAIR Voice Pipeline Repo](https://github.com/MohamedTarekMostafa/Realtime-AI-Voice-Assistance)

---

### ⚡ What makes the Realtime API special?
Most voice bots convert your voice to text, process it, and then convert it back to speech. That's slow. By using the **Gemini 2.5 Flash Native Audio** model, this assistant:

* **Low Latency:** Responds in milliseconds. It feels like a real phone call.
* **Audio Intelligence:** It doesn't just read words; it hears if you're stressed, happy, or in a hurry.
* **True Fluidity:** It handles the "natural flow" of speech—you can interrupt it, and it will react just like a human concierge.

---

### 🛠️ How I put it together
* **Engine:** `gemini-2.5-flash-native-audio-preview` (The secret sauce for native audio).
* **Infrastructure:** **LiveKit Agents** for seamless WebRTC audio streaming.
* **Persona:** A custom-coded EGYPTAIR concierge that stays professional and welcoming.

---

### 💻 Set it up yourself
1.  **Clone & Install:**
    ```bash
    pip install livekit-agents livekit-plugins-google python-dotenv
    ```
2.  **Keys:** Add your `GOOGLE_API_KEY` and `LIVEKIT` credentials to a `.env` file.
3.  **Launch:**
    ```bash
    python main.py dev
    ```

---

### 🌍 Future Flight Path
I'm planning to connect this directly to flight data systems so it can handle real-time booking and gate updates through the same Realtime API interface.

---
*Made with ❤️ for the future of travel.*



