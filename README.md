"# ASHA" 
An open-source AI-powered solution designed to improve maternal and child healthcare access in rural India using voice-first technology, SMS/IVR interfaces, and multilingual support. Built with low-resource environments in mind.

---

## 🚀 Features

- **Voice & SMS Support:** Accessible via toll-free number or basic phone using voice (IVR) and keypad inputs.
- **Multilingual AI Agent:** Powered by Whisper + Indic TTS + LLaMA/Vicuna for natural, regional language conversations.
- **Aadhaar-based Login:** Users log in using Aadhaar; ASHA/Doctor with unique ID.
- **Pregnancy Tracker:** Monthly reminders, risk detection, and personalized nudges.
- **Family Health Profiles:** Auto-fetched via Aadhaar; includes maternal, child, elderly support.
- **AI Health Summaries:** Doctors see auto-summarized records; ASHAs get task checklists.
- **Document Scanner & Scheme Filler:** OCR-based auto-form fill and scheme suggestions.
- **Meal Plans & Local Tips:** AI suggests affordable diets using local ingredients and markets.
- **Offline-First:** Syncs when connected; works even in low/no-internet regions.
- **Open Standards & Interoperability:** FHIR-compliant, integrates with ABHA/eSanjeevani.

---

## 🛠️ Tech Stack

| Layer           | Technologies Used |
|----------------|-------------------|
| AI Models       | LLaMA, Vicuna, FastText, Naive Bayes, TensorFlow |
| Voice & Speech  | Whisper, Coqui ASR, Indic TTS |
| Backend         | LangChain, FastChat API, FHIR API, PostgreSQL |
| Document Tools  | Tesseract OCR |
| Communication   | Twilio/Exotel (SMS/IVR), USSD |
| Frontend        | React Native / Flutter (Mobile) |
| Deployment      | MeghRaj, Local Servers (Gov Cloud) |

---

## 📦 Datasets Used

- MoHFW Family Health Survey Data (Public)
- RMNCH+A Indicators (Govt)
- NFHS-5 Dataset (Kaggle)
- ICMR Public Health Guidelines
- User-generated data via interaction
- Synthetic data generated for testing edge-cases
