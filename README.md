#  EGYPTAIR Realtime API: Next-Gen Voice Experience

This project is an exploration of what's possible when you combine **Google’s Gemini 2.5 Flash Realtime API** with **LiveKit**. I’ve built a voice concierge for EGYPTAIR that processes audio natively—meaning it hears, thinks, and speaks in real-time without the lag of traditional "speech-to-text" loops.

---

### 📺 The Demo

https://github.com/user-attachments/assets/bbeaef0f-0359-410b-ad27-ddcefb6487f0

> *Watch how the Realtime API handles natural interruptions and emotional cues.*

---

###  What makes the Realtime API special?
Most voice bots convert your voice to text, process it, and then convert it back to speech. That's slow and robotic. 

By using the **Gemini 2.5 Flash Native Audio** model, this assistant:
* **Low Latency:** Responds in milliseconds. It feels like a phone call, not a walkie-talkie.
* **Audio Intelligence:** It understands the nuances of your voice—if you're stressed, happy, or in a hurry.
* **Fluid Conversations:** It handles the "natural flow" of speech, including the ability to greet you warmly and provide concierge-level service.

---

###  How I put it together
* **Engine:** `gemini-2.5-flash-native-audio-preview` (The secret sauce for the Realtime API).
* **Infrastructure:** **LiveKit Agents** for seamless WebRTC audio streaming.
* **Persona:** A custom-coded EGYPTAIR concierge that stays professional and welcoming.

---

###  Set it up yourself
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

###  Future Flight Path
I'm planning to connect this directly to flight data systems so it can handle real-time booking and gate updates through the same Realtime API interface.

---

*Made for the future of travel. *



