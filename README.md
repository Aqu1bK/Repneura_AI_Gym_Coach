<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.54-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/MediaPipe-Pose_Detection-orange?style=for-the-badge&logo=google" alt="MediaPipe">
  <img src="https://img.shields.io/badge/Qwen2.5-AI_Coach-412991?style=for-the-badge&logo=openai" alt="Qwen">
  <img src="https://img.shields.io/badge/OpenRouter-API_Gateway-635BFF?style=for-the-badge&logo=openai" alt="OpenRouter">
  <img src="https://img.shields.io/badge/WebRTC-Live_Video-333333?style=for-the-badge&logo=webrtc" alt="WebRTC">
  <img src="https://img.shields.io/badge/Streamlit_Cloud-Live-FF4B4B?style=for-the-badge&logo=streamlit" alt="Live">
</div>

<br />

# 🏋️ Repneura

### AI-Powered Real-Time Gym Coach

Your personal AI fitness coach that watches your form through your webcam in real-time. Select any exercise, set your goals, and Repneura tracks every rep with precision — counting your movements, measuring joint angles, analyzing your depth, and giving AI-powered feedback to perfect your form. Powered by Qwen2.5-Instruct via OpenRouter for intelligent exercise coaching. No wearables, no sensors — just your camera and AI.

<p align="center">
  <a href="https://repneura.streamlit.app/" target="_blank">
    <strong>🌐 Try it Live → repneura.streamlit.app</strong>
  </a>
</p>

---

## 🎥 30-Second Demo Walkthrough

| Step | Action | What You'll See |
|:----:|--------|-----------------|
| **1** | Open [Live App](https://repneura.streamlit.app/) | Landing page with session setup |
| **2** | Enter your name → Click **Start Session** | Dashboard with sidebar controls |
| **3** | Select Exercise (Squat/Push-up), Sets & Reps per set | Workout plan configured |
| **4** | Click **Start Workout** → Allow camera | Live webcam feed with AI skeleton overlay |
| **5** | Start exercising! | Watch real-time rep counting, joint angles, and AI feedback |

---

## ✨ What Repneura Tracks in Real-Time

### 📊 **Live Workout Progress**
| Metric | What It Shows |
|--------|---------------|
| **Total Reps** | Cumulative reps across all sets |
| **Current Set Reps** | Reps completed in the active set |
| **Sets Complete** | Number of sets finished out of target |

### 🦴 **Exercise Metrics (Per Frame)**
| Metric | Description | Why It Matters |
|--------|-------------|----------------|
| **Knee Angle** | Angle at knee joint in degrees | Tracks squat depth & leg press form |
| **Back Angle** | Torso inclination relative to vertical | Monitors spine alignment & safety |
| **Depth Status** | Real-time depth assessment | Ensures you're hitting proper range of motion |

### 🎯 **AI Coach Features**
- **Automatic Rep Counting** — Detects when you complete a full rep
- **Form Analysis** — Qwen2.5-Instruct evaluates your posture frame-by-frame
- **Real-Time Overlay** — See your skeleton tracking on the live video feed
- **Audio Feedback** — AI-powered voice guidance using gTTS

---

## 🏗️ Real-Time AI Pipeline

```
┌────────────────────────────────────────────────────────────────────┐
│                      LIVE WORKOUT SESSION                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐    ┌──────────────┐    ┌─────────────────────────┐   │
│  │  Webcam  │───▶│   WebRTC     │───▶│   MediaPipe Pose        │   │
│  │  Feed    │    │   Stream     │    │   33 Body Landmarks     │   │
│  └──────────┘    └──────────────┘    └───────────┬─────────────┘   │
│                                                   │                 │
│                    ┌──────────────────────────────┘                │
│                    ▼                                               │
│  ┌─────────────────────────────────────────────┐                  │
│  │         Exercise Analysis Engine            │                  │
│  ├─────────────────────────────────────────────┤                  │
│  │  • Rep Counter (movement pattern detection) │                  │
│  │  • Joint Angle Calculator (knee, back)      │                  │
│  │  • Depth Classifier (shallow/parallel/deep) │                  │
│  │  • Set Tracker (auto-set progression)       │                  │
│  └─────────────────────┬───────────────────────┘                  │
│                        ▼                                           │
│  ┌─────────────────────────────────────────────┐                  │
│  │    Qwen2.5-Instruct via OpenRouter          │                  │
│  │    (OpenAI SDK Compatible)                   │                  │
│  │  Form analysis → Feedback generation → gTTS │                  │
│  └─────────────────────────────────────────────┘                  │
│                        ▼                                           │
│  ┌─────────────────────────────────────────────┐                  │
│  │          Streamlit Dashboard                 │                  │
│  │  Live video + Metrics + Progress + Feedback  │                  │
│  └─────────────────────────────────────────────┘                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

| Technology | Role | Why This Stack |
|------------|------|----------------|
| **Streamlit** | Web UI & session management | Fastest way to build interactive data apps |
| **streamlit-webrtc** | Real-time camera streaming | Low-latency video processing in browser |
| **MediaPipe Pose** | 33-point body landmark detection | Google's state-of-the-art pose estimation |
| **OpenCV** | Frame processing & overlay rendering | Industry standard for computer vision |
| **Qwen2.5-Instruct** | Exercise form analysis & coaching | Advanced open-source LLM with strong reasoning via OpenRouter |
| **OpenRouter API** | AI model access gateway | Unified API with OpenAI SDK compatibility |
| **OpenAI SDK** | LLM integration layer | Clean interface to call Qwen2.5 through OpenRouter |
| **gTTS** | Text-to-speech audio feedback | Hands-free coaching during exercise |
| **Pandas** | Session data tracking | Structured workout metrics logging |

---

## 🎯 Key Features That Set Repneura Apart

### 🤖 **Truly Intelligent Coaching**
- Not just counting reps — **analyzing form quality**
- Qwen2.5-Instruct understands proper exercise biomechanics
- Gives specific, actionable feedback (not generic tips)
- OpenRouter integration ensures reliable, fast AI responses

### ⚡ **Zero Latency Experience**
- WebRTC streaming for sub-second video processing
- Pose detection runs at 15-30 FPS
- Metrics update in real-time as you move
- AI feedback generated asynchronously to avoid frame drops

### 🎛️ **Fully Customizable Workouts**
- Choose any exercise from the library
- Set your own sets × reps targets
- Auto-progresses through sets as you complete them

### 📈 **Live Visual Feedback**
- Skeleton overlay confirms the AI can see you properly
- Color-coded joint angles show form quality at a glance
- Progress bars track sets and reps completion

---

### 🧠 AI Coach Feedback Generation
```
Joint angles + Depth status + Set progress 
→ Sent to Qwen2.5-Instruct via OpenRouter (OpenAI SDK format)
→ AI analyzes form quality & provides coaching cues
→ Feedback converted to speech via gTTS for hands-free guidance
```

---

## 📊 Live Dashboard Layout

```
┌──────────────────────────────────────────────────────────┐
│  🏋️ REPNEURA AI GYM COACH                                │
├────────────────────┬─────────────────────────────────────┤
│    LEFT SIDEBAR    │          MAIN CANVAS                │
│                    │                                     │
│  📋 WORKOUT PLAN   │  ┌─────────────────────────────┐   │
│  • Exercise: Squat │  │                             │   │
│  • Sets: 3         │  │    LIVE WEBCAM FEED          │   │
│  • Reps: 10        │  │    with skeleton overlay     │   │
│                    │  │    + rep count badge         │   │
│  📊 PROGRESS       │  │                             │   │
│  • Total Reps: 15  │  └─────────────────────────────┘   │
│  • Set Reps: 5/10  │                                     │
│  • Sets Done: 1/3  │  ┌─────────────────────────────┐   │
│                    │  │  🦴 EXERCISE METRICS        │   │
│  🦴 METRICS        │  │  Knee Angle: 95°  ✅        │   │
│  (live per frame)  │  │  Back Angle: 12°  ✅        │   │
│  • Knee Angle      │  │  Depth: DEEP      🟢       │   │
│  • Back Angle      │  └─────────────────────────────┘   │
│  • Depth Status    │                                     │
│                    │  ┌─────────────────────────────┐   │
│                    │  │  🤖 Qwen2.5 AI COACH        │   │
│                    │  │  "Great depth! Keep your     │   │
│                    │  │   chest up on the way up"    │   │
│                    │  └─────────────────────────────┘   │
└────────────────────┴─────────────────────────────────────┘
```

---

## 🚀 Why Recruiters Will Love This Project

| Quality | Evidence |
|---------|----------|
| **Production-Ready** | Live on Streamlit Cloud, handles real webcam streams |
| **Real AI/ML** | MediaPipe pose detection + Qwen2.5-Instruct via OpenRouter |
| **Multi-Provider AI** | OpenRouter integration shows API gateway experience |
| **Complex Integration** | WebRTC streaming + Computer Vision + LLM + TTS in one pipeline |
| **User-Centric Design** | Intuitive sidebar controls, real-time visual feedback |
| **Performance** | Real-time processing at 15-30 FPS with pose detection |
| **Problem Solving** | Addresses real fitness pain point — form correction without expensive trainer |
| **Modern AI Stack** | Uses latest open-source LLM with OpenAI SDK compatibility |

---

## 📁 Project Structure

```
repneura/
├── app.py                      # Main Streamlit application
├── requirements.txt            # All dependencies
├── .env                        # OpenRouter API key
├── utils/
│   ├── pose_detector.py       # MediaPipe pose landmark extraction
│   ├── exercise_analyzer.py   # Rep counting, angle calculation, depth classification
│   ├── ai_coach.py            # Qwen2.5-Instruct via OpenRouter (OpenAI SDK)
│   └── audio_feedback.py      # gTTS text-to-speech coaching
└── .streamlit/
    └── config.toml             # Streamlit Cloud configuration
```

---

## 🌐 Live Access

<div align="center">

| | |
|-------------------|------------------------------------------|
| **Live URL** | [repneura.streamlit.app](https://repneura.streamlit.app/) |
| **Platform** | Streamlit Cloud |
| **AI Models** | MediaPipe Pose + Qwen2.5-Instruct (via OpenRouter) |
| **Status** | 🟢 Live & Processing Real-Time Video |

### 🎯 Open the app, allow camera, and start exercising — AI watches your form instantly!

</div>

---

## 💡 Tips for Testing the Live App

1. **Use a well-lit room** — MediaPipe needs to see your full body clearly
2. **Stand 6-8 feet from camera** — Ensures your entire body is in frame
3. **Wear contrasting clothes** — Helps with landmark detection accuracy
4. **Try Squats first** — Most dramatic joint angle changes, easiest to see AI working
5. **Watch the metrics panel** — See knee angle change in real-time as you squat
6. **Speak your rep count** — Compare your count vs AI's automatic detection
7. **Listen for AI feedback** — Qwen2.5 analyzes your form and gives coaching cues

---

## 🏆 Technical Achievements

- 🔧 Built real-time pose estimation
- 🧠 Integrated Qwen2.5-Instruct via OpenRouter for domain-specific exercise coaching
- 🌐 Demonstrated multi-provider AI integration using OpenAI SDK with OpenRouter gateway
- 📹 Implemented browser-based WebRTC streaming for computer vision
- ⚡ Achieved 15-30 FPS processing with MediaPipe on CPU
- 🎤 Added voice feedback via gTTS for truly hands-free coaching experience

---

<div align="center">
  <p>Built with ❤️ to make personal training accessible to everyone</p>
  <p>
    <a href="https://repneura.streamlit.app/"><strong>🔗 Try Live App Now</strong></a> •
    <a href="#-30-second-demo-walkthrough">Quick Demo</a> •
    <a href="#-real-time-ai-pipeline">How It Works</a>
  </p>
</div>
